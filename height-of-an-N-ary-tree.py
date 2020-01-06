# python3

import sys
import threading
import collections

class Node:
    def __init__(self, data = None):
        self.data = data
        self.child = None

def treeHeight(node, nodes):
    
    node_height = 0
    
    if node.data in nodes:
    
        for i in range(len(nodes[node.data])):
            node.child = treeHeight(Node(nodes[node.data][i]), nodes)
            node_height = max(node.child, node_height)

    return 1 + node_height

def compute_height(n, parents):
    
    nodes = collections.defaultdict(list)

    for i, node in enumerate(parents):
        nodes[node].append(i)

    head = Node(nodes[-1][0])

    return treeHeight(head, nodes)


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

    # t = open("C:\\Users\\glory\\Downloads\\Data_Structures\\week1_basic_data_structures\\2_tree_height\\tests\\20")
    # n = int(t.readline())
    # parents = list(map(int, t.read().split()))
    # print(compute_height(n, parents))  
