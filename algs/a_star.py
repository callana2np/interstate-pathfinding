# Author: Aidan Callan
import math
import heapq

def haversine(c1,c2):
    lon1,lat1 = c1
    lon2,lat2 = c2

    r = 3958.8 # radius of Earth in miles

    # convert to radians
    lat1_rads = math.radians(lat1)
    lon1_rads = math.radians(lon1)
    lat2_rads = math.radians(lat2)
    lon2_rads = math.radians(lon2)

    # differences of latitude and longitude in radians
    d_lat = lat2_rads - lat1_rads
    d_lon = lon2_rads - lon1_rads

    radicand = math.sin((d_lat)/2)**2 + math.cos(lat1_rads)*math.cos(lat2_rads)*math.sin((d_lon)/2)**2

    return 2 * r * math.asin(math.sqrt(radicand)) # haversine formula

def build_path(backtrack,dest):
    path = [dest] # start with destination node
    while dest in backtrack:
        dest = backtrack[dest] # update current node to its parent node
        path.append(dest) # append parent to path
    path.reverse() # reverse from end->start to start->end
    return path

def a_star(sys,src,dest):
    graph = sys.graph
    coords = sys.coordinates
    dest_coords = coords[dest]

    o_set = [] # p-queue of (f-score,node) for nodes to be visited
    c_set = set() # closed set for nodes already visited
    heapq.heappush(o_set,(0,src)) # push distance of 0 with assoc starting node to open set

    g = {} # dictionary for shortest known distance from src node to all other nodes
    for n in graph.nodes:
        g[n] = math.inf
    g[src] = 0

    backtrack = {} # maps nodes to parent for reconstructing path

    while len(o_set)>0:
        f,curr = heapq.heappop(o_set) # pop node with lowest f-score
        if curr in c_set: continue # skip iteration if node already visited with better path
        c_set.add(curr) # mark current node as visited
        if curr == dest: return build_path(backtrack,curr),g[dest],c_set # shortest path found
        for n in graph.neighbors(curr):
            if n in c_set: continue # don't revisit closed neighbor
            n_coords = coords[n]
            if n!=dest and graph.nodes[n].get("loc"): continue # if neighbor is a city that isn't destination, skip
            dist = graph[curr][n].get("distance")
            g_temp = g[curr] + dist # candidate cost for reaching neighbor
            if g_temp < g[n]: # if candidate cost lower than current g value, update
                g[n] = g_temp
                backtrack[n] = curr
                heur = 0.7*haversine(n_coords,dest_coords)
                f = g[n] + heur # core formula: f(n)=g(n)+h(n)
                heapq.heappush(o_set,(f,n)) # push neighbor and estimated cost onto open set
    
    return [],-1,c_set # default