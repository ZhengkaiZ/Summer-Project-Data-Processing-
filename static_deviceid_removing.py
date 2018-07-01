'''author Zhengkai Zhang
   this code is to get static node of one node.
'''
import sys
import numpy as np
import networkx as nx
from networkx.drawing.nx_agraph import write_dot
#import matplotlib.pyplot as plt
import pylab as plt #import Matplotlib plotting interface >>>
from sets import Set
from collections import deque

# Read from 4 to 6 o'clock to get the static device name
def get_static_device(file_name, time_from, time_to):
    with open(file_name) as f:
        while (True):
            line = f.readline().split(" ");
            if (len(line) < 3):
                continue
            if (line[0] == '*') & ((line[2].split(':')[0] == time_from)):
                break
        static_device = Set();
        while (True):
            line = f.readline().split(" ");
            if (line[0] == '*'):
                if (line[2].split(':')[0] == time_to):
                    break
                else:
                    continue
            static_device.add(line[0])
    return static_device

def read_device(file_name, static_device):
    device_list = [];
    block = -1;
    with open(file_name) as f:
        for line in f.readlines():
            list = line.split(" ")
            if (list[0] == '*'):
                block += 1
                device_list.append(Set())
                continue
            else:
                if (list[0] in static_device):
                    continue
                device_list[block].add(list[0])

    return device_list


def time_switch(desired_time):
    return (desired_time + 4) * 6 * 60

def connectivity_at_certain_time(time, device_list):
    device_count = len(device_list)
    dict = {}
    length = length = len(device_list);
    for i in range(0, length):
        temp_set = device_list[i]
        for entry in temp_set[time]:
            for j in range(0, length):
                if (j == i):
                    continue
                for x in range (1, 6):
                    if (entry in device_list[j][time + x]):
                        if (dict.get(str(i) + " " + str(j)) == None):
                            dict[str(i) + " " + str(j)] = 1
                        else:
                            dict[str(i) + " " + str(j)] += 1
    return dict

def dictToGraph(dict):
    G = nx.MultiDiGraph()

    for key in dict.keys():
        pos = key.split(" ")
        G.add_edge(pos[0], pos[1], label=str(dict.get(key)))
    return G

def main():
    time_from = '02';
    time_to = '06';
    static_device = []
    device_list = []
    # 0 : node 11
    # 1 : node 6
    # 2 : node 7
    # 3 : node 9
    for i in range(1, 10):
        file_name = sys.argv[i]
        static_device.append(get_static_device(file_name, time_from, time_to));
        device_list.append(read_device(file_name, static_device[i - 1]));
    dict = connectivity_at_certain_time(time_switch(18), device_list);
    G = dictToGraph(dict)
    write_dot(G, 'graph.dot')
if __name__ == '__main__':
    main()


