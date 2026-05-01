# Dijkstra's vs. A* Search: Route Optimization
## Description
This is a graph-based interstate highway system simulator implementing and comparing Dijkstra's and A* search algorithms to compute optimal routes between cities. The project demonstrates performance trade-offs between uniform and heuristic search on real-world-like geodata.

## Features
* Implements A* search and Dijkstra's algorithms for route optimization
* Models the U.S. Interstate Highway System as a graph using the NetworkX Python library
* Uses real geographic coordinates to calculate distances and heuristics
* Highlights performance differences and trade-offs between classic uninformed and heuristic search
* Interactive GUI with hover tooltips to identify nodes (cities/interchanges)
* Displays output route directly on map

## How to Run
### 1. Download repository
1. Click the "Code" button on repository page.
2. Select "Download ZIP"
3. Extract files to PC

### 2. Install dependencies
This project requires the networkx and matplotlib Python libraries. They can be installed with the following command:
```
pip install networkx matplotlib
```
Tkinter is included with most Python installations.

### 3. Run program
```
python main.py # or python3 main.py (if Mac/Linux)
```

### 4. Enter input
A dialog box will appear prompting you to enter the starting city and destination city. City names must match those defined in the system.
Examples:
* Boston, MA
* New York, NY
* Jacksonville, FL
* Denver, CO
* Los Angeles, CA
Please refer to the source code (cities.py) for the full list of supported cities.

### 5. View results
After entering input:
* The calculated routes and total distances for both algorithms are printed to the terminal
* An interactive map opens to display the routes
* The route is highlighted in a distinct color
* All cities are shown as green nodes
* Hover over nodes to view city/interchange names.

## Example Output
```
===A* SEARCH ALGORITHM===
A* searched 13 nodes
Total distance: 198 miles
Route:  New York, NY -> I-87/I-95 -> I-91/I-95 -> I-84/I-91 -> I-84/I-90 -> I-90/I-95 -> Boston, MA

===DIJKSTRA'S ALGORITHM===
Dijkstra's searched 271 nodes
Total distance: 198 miles
Route:  New York, NY -> I-87/I-95 -> I-91/I-95 -> I-84/I-91 -> I-84/I-90 -> I-90/I-95 -> Boston, MA
```
This example underlines how A* search finds the same optimal route while exploring significantly less nodes than Dijkstra's algorithm.

## Future Improvements
* Expand the dataset with additional cities and road connections
* Introduce heuristic scaling factor for A* to analyze performance and optimality
* Replace dialog input with full GUI