# Author: Aidan Callan
import math
import networkx as nx
import matplotlib.pyplot as plt
from tkinter import simpledialog
from algs.a_star import a_star
from algs.dijkstra import dijkstra

class RoadSystem:
    def __init__(self):
        self.graph = nx.Graph()
        self.coordinates = {}

    # add a node for interchange of two roads
    def add_interchange(self,interchange,city,lat,lon):
        self.graph.add_node(interchange,city=city)
        self.coordinates[interchange] = (lon,lat)

    # add an edge (road) connecting two nodes (interchanges/cities)
    def add_interstate(self,interchange1,interchange2,highway,distance):
        self.graph.add_edge(interchange1,interchange2,highway=highway,distance=distance)

    # add a city node
    def add_city(self,city,interchange_arr,lat,lon):
        self.graph.add_node(city,loc=True) # "loc" attribute denotes whether node is city or interchange
        self.coordinates[city] = (lon,lat)
        for interchange in interchange_arr:
            self.graph.add_edge(city,interchange,highway="exit",distance=0) # connect interchange to associated city with distance of 0 on edge

    # print road system
    def print_system(self):
        for start,end,data in self.graph.edges(data=True):
            print(f"{start} <-> {end} via {data['highway']} ({data['distance']} miles)")

    # get user input for source and destination cities to run algorithms
    def get_route_input(self):
        src = simpledialog.askstring("Input","Source city:")
        dest = simpledialog.askstring("Input","Destination city:")

        if src not in self.graph or dest not in self.graph:
            print("Source city and/or destination city not recognized.")
            return
        
        # running A*
        print("\n===A* SEARCH ALGORITHM===")
        a_path,a_dist,a_visited = a_star(self,src,dest)
        print(f"A* searched {len(a_visited)} nodes\nTotal distance: {a_dist} miles")
        self.highlight_route(a_path,"blue",title=f"{src} to {dest} using A* Search Algorithm") # highlight A* route in blue

        # running Dijkstra's
        print("\n===DIJKSTRA'S ALGORITHM===")
        d_path,d_dist,d_visited = dijkstra(self,src,dest)
        print(f"Dijkstra's searched {len(d_visited)} nodes\nTotal distance: {d_dist} miles")
        self.highlight_route(d_path,"red",title=f"{src} to {dest} using Dijkstra's Algorithm") # highlight Dijkstra's route in red

    # color route edges on map
    def highlight_route(self,path,edge_color,title):
        print("Route: ",end=" ")
        for n in path[:-1]:
            print(f"{n} ->",end=" ")
        print(path[-1])

        fig, axes = plt.subplots(figsize=(10,6))

        # set of city nodes
        city_nodes = set()
        for n,d in self.graph.nodes(data=True):
            if d.get("loc"): city_nodes.add(n)

        # style cities as large green nodes
        nx.draw_networkx_nodes(self.graph,self.coordinates,nodelist=city_nodes,node_color="green",node_size=20,ax=axes)

        # color graph edges black
        nx.draw_networkx_edges(self.graph,self.coordinates,width=1,edge_color="black",ax=axes)

        # set of edges
        route_edges = set()
        for i in range(len(path)-1):
            route_edges.add((path[i],path[i+1]))
        nx.draw_networkx_edges(self.graph,self.coordinates,edgelist=route_edges,width=2,edge_color=edge_color,ax=axes) # bold route edges

        # annotation tooltip shown only when hovered over by cursor
        annotation = axes.annotate("",xy=(0,0),xytext=(10,10),textcoords="offset points",bbox=dict(boxstyle="round",fc="w"),arrowprops=dict(arrowstyle="->"))
        annotation.set_visible(False)

        # event handler for hovering over node
        def on_hover(event):
            if event.inaxes:
                x,y = event.xdata,event.ydata # get cursor position

                # get node closest to cursor
                closest = None
                min_dist = math.inf
                for n in self.coordinates:
                    node_x,node_y = self.coordinates[n]
                    dx = node_x - x
                    dy = node_y - y
                    dist = dx**2 + dy**2 # squared distance
                    if dist<min_dist:
                        min_dist = dist
                        closest = n

                node_dist = ((self.coordinates[closest][0]-x)**2 + (self.coordinates[closest][1]-y)**2)**0.5 # calculate distance from cursor to node using euclidean dist formula

                # make annotation visible if distance within 0.5 units
                if node_dist < 0.5:
                    annotation.set_text(closest)
                    annotation.xy = self.coordinates[closest]
                    annotation.set_visible(True)
                # hide annotation otherwise
                else:
                    annotation.set_visible(False)
                
                fig.canvas.draw_idle() # redraw figure after mouse event

        fig.canvas.mpl_connect("motion_notify_event",on_hover) # connect event handler to figure

        plt.title(title)
        plt.show()