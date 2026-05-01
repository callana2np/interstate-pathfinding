# Author: Aidan Callan

import heapq
import math

def build_path(backtrack,dest):
        path = [dest] # start with dest
        # while current node in dictionary, add its parent on route to path
        while dest in backtrack:
            dest = backtrack[dest]
            path.append(dest)
        path.reverse() # reverse from end->start to start->end
        return path

def dijkstra(sys,src,dest):
    graph = sys.graph

    dist = {} # dictionary for storing shortest distance from src to all other nodes
    for n in graph.nodes:
        dist[n] = math.inf # initialize all distances to max value
    dist[src] = 0 # distance from src to src is 0

    # priority queue
    pq = []
    heapq.heappush(pq,(0,src)) # push source node and its distance of 0

    c_set = set() # visited nodes with finalized shortest difference
    backtrack = {} # dictionary to store parents on route

    while(len(pq)>0):
        d,v = heapq.heappop(pq) # pop lowest known distance and its node from priority queue
        if(v in c_set): continue # if node visited, skip iteration
        c_set.add(v) # mark node as visited
        if(d>dist[v]): continue # if popped distance farther than that already stored, skip iteration
        for n in graph.neighbors(v):
            if n!=dest and graph.nodes[n].get("loc"): continue # if node is a city that isn't destination, skip iteration
            edge_dist = graph[v][n].get("distance") # get edge's distance
            if(edge_dist+dist[v]<dist[n]): # check if shorter path to neighbor found
                backtrack[n] = v # store parent of neighbor for backtracking
                dist[n] = dist[v] + edge_dist # store new shortest distance for this neighbor 
                heapq.heappush(pq,(dist[n],n)) # push neighbor into priority queue
    
    return build_path(backtrack,dest),dist[dest],c_set