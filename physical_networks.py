import sys
import networkx as nx
import pylab as plt
from sets import Set
from networkx.drawing.nx_agraph import write_dot

hh_node = [6, 7, 9, 11]
hh = [[7, 9, 11], [6, 9], [6, 7], [6]]

def build_physical_network():
    g = nx.MultiDiGraph()
    flag = 0
    for node in hh_node:
        for n in hh[flag]:
            g.add_edge(node, n)
        flag += 1
    return g

def main():
    g = build_physical_network()
    nx.write_gexf(g, 'physical.gexf')

if __name__ == '__main__':
    main()
