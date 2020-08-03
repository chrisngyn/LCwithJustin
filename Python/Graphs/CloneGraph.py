"""
All I got to say is - I HATE GRAPHS

so, all trees are graphs. but not all graphs are trees!

how do we represent a tree? we have a node class with a .left and a .right property for example

but how do we represent a graph? the commons ways are to use an adjacency list (have an array with all the nodes its connected to) or an adjacency matrix (2d array)

a connected graph - you can access all nodes through any of the nodes in the graph

--------------------------------------------------

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
"""

from collections import deque

class GraphNode:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    
def cloneGraph(node: GraphNode) -> GraphNode:
    ret = GraphNode(node.val)
    dummy = ret
    queue = deque([node])

    while len(queue) > 0:
        current_node = queue.popleft()
        dummy = GraphNode(current_node.val)

        for item in current_node.neighbors:
            new_node = GraphNode(item.val)
            dummy.neighbors.append(item)
            queue.append(item)
        
        ret.neighbors.append(dummy)
    
    return ret

def printGraphBFS(node: GraphNode):
    queue = deque([node])

    while len(queue) > 0:
        current = queue.popleft()
        print(current.val)

        for item in current.neighbors:
            queue.append(item)


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