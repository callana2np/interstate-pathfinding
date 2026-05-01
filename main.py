# Author: Aidan Callan

from road_system import RoadSystem
from geodata.interchanges import load_interchanges
from geodata.interstates import load_interstates
from geodata.cities import load_cities

interstate_system = RoadSystem()

# interchange nodes
load_interchanges(interstate_system)

# interstate roads (edges)
load_interstates(interstate_system)

# city nodes
load_cities(interstate_system)

# print all nodes, edges, and distances
interstate_system.print_system()

# get route input and display graph
interstate_system.get_route_input()