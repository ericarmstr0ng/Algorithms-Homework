# ******************************************************************************************
# Wrestlers
# Author: Eric Armstrong
# Date: 2/17/19
# Course: CS 325
# Description: Program determines if given wrestlers can be rivals based on matches
# ******************************************************************************************


from collections import OrderedDict
import sys


# ******************************************************************************************
# Procedure: barp (Barpitite check)
# Description: Determines if graph vertices can be divided into two independent sets
# Citation: https://www.geeksforgeeks.org/bipartite-graph/
# ******************************************************************************************

def barp(graph, v):
    queue = graph[v][1]
    u = queue[0]
    while queue:
        if graph[u][0] == -1:
            graph[u][0] = 1 - graph[v][0]
            barp(graph, u)
        elif graph[u][0] == graph[v][0]:
            return False
        u = queue.pop()

    return True

# ******************************************************************************************
# Procedure: Wrestler
# Description: Reads input file of wrestlers and rivalries
#              and determines if it is possible for such rivalries to exist
# ******************************************************************************************

def fights(input_file):
    file = open(input_file)
    num_wrestlers = int(file.readline().strip())
    wrestlers = OrderedDict()

    # Initialize graph
    for fighters in range(num_wrestlers):
        wrestlers[file.readline().strip()] = [-1, []]

    num_matches = int(file.readline().strip())

    # Create graph of bouts in text file
    for bouts in range(num_matches):
        match = (list(str(x) for x in file.readline().strip().split()))
        wrestlers[match[0]][1].append(match[1])
        wrestlers[match[1]][1].append(match[0])

    possible = True
    first = 0
    Baby = []
    Heel = []

    # for every vertices check Bipartite quality
    for key, value in wrestlers.items():
        if wrestlers[key][0] == -1:
            # if there is only a single connection place fighters in opposite groups
            if len(wrestlers[key][1]) == 1:
                wrestlers[key][0] = 1
                wrestlers[wrestlers[key][1][0]][0] = 0
            # Set first fighter to Babyface
            elif first == 0:
                wrestlers[key][0] = 1
                first = -1

            if not barp(wrestlers, key):
                possible = False
                break
        if wrestlers[key][0] == 1:
            Baby.append(key)
        else:
            Heel.append(key)

    if possible:
        print('Yes Possible')
        print('Babyfaces: {}'.format(' '.join(str(x) for x in Baby)))
        print('Heels: {}'.format(' '.join(str(x) for x in Heel)))
    else:
        print("Impossible")


fights(str(sys.argv[1]))

