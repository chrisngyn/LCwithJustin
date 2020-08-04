"""
all I got to say is - I HATE GRAPHS

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
    if node == None:
        return None
    
    clones = {node : GraphNode(node.val)}  # map original node to cloned node
    queue = deque([node])
    
    while len(queue) > 0:
        current_node = queue.popleft()  # this is the ORIGINAL node. first, check if in dictionary, if not, add, append neighbours to the clone

        for item in current_node.neighbors:
            if item not in clones:  # if there's a neighbour of our original node that isn't in the dictionary...
                clones[item] = GraphNode(item.val)  # we'll add it, and map it to a deep copy
                queue.append(item)
            
            clones[current_node].neighbors.append(clones[item])  # clones[item] gives us the deep copy of the node, so then we append all the deep copy neighbours to it
    
    return clones[node]

def printGraphBFS(node: GraphNode):
    queue = deque([node])
    seen = set([node])

    while len(queue) > 0:
        current_node = queue.popleft()

        print(current_node.val)

        for item in current_node.neighbors:
            if item not in seen:
                queue.append(item)
                seen.add(item)

"""
1 -- 3
     |
2 -- 4

expected: 1, 3, 4, 2

we'll make a deep clone of this, then we'll modify the original graph, then we'll print BFS of both graphs and see if they're different
"""
node1 = GraphNode(1)
node2 = GraphNode(2)
node3 = GraphNode(3)
node4 = GraphNode(4)
node1.neighbors = [node3]
node2.neighbors = [node4]
node3.neighbors = [node1, node4]
node4.neighbors = [node2, node3]
deep_copy = cloneGraph(node1)
node2.val = 99
print("DEEP COPY GRAPH:")
printGraphBFS(deep_copy)
print("")
print("MODIFIED ORIGINAL GRAPH:")
printGraphBFS(node1)
