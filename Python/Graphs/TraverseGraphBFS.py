"""
Traversing a graph using Breadth First Search.
"""

from collections import deque

class GraphNode:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        # if neighbors == None:
        #     self.neighbors = []
        # else:
        #     self.neighbors = neighbors
        self.neighbors = neighbors if neighbors is not None else []

def printGraphBFS(node: GraphNode):
    queue = deque([node])

    while len(queue) > 0:
        # WAIT OMG THIS DOESN'T WORK IF IT'S ALL CONNECTED NOOOOO WTF
        # ok rip iwant2 die


    queue = deque([node])

    while len(queue) > 0:
        current_node = queue.popleft()

        print(current_node.val)

        for node in current_node.neighbors:
            queue.append(node)

root = GraphNode(1)
node2 = GraphNode(2)
node3 = GraphNode(3)
node4 = GraphNode(4)
root.neighbors = [node3]
node3.neighbors = [node4]
node4.neighbors = [node2]
deep_copy = cloneGraph(root)
node2.val = 99
print('NORMAL GRAPH (with modified 99)')
printGraphBFS(root)
print('DEEP COPY')
printGraphBFS(deep_copy)

"""
1 ----- 3
        |       
2 ----- 4

expected 1 - 3 - 4 - 2
"""