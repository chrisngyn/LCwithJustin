# Traversing a graph with Breadth First Search.
# Generally the same approach as with a tree, except you need to store all your seen nodes so you don't revisit them.

from collections import deque

class GraphNode:
    def __init__(self, val=0, neighbours=None):
        self.val = val
        if neighbours == None:
            self.neighbours = []
        else:
            self.neighbours = neighbours

def printGraphBFS(node: GraphNode):
    queue = deque([node])
    seen = set([node])

    while len(queue) > 0:
        current_node = queue.popleft()

        print(current_node.val)

        for item in current_node.neighbours:
            if item not in seen:
                queue.append(item)
                seen.add(item)

"""
1 -- 2    5
  \- 3 -/
  \- 4 -/

expected: 1, 2, 3, 4, 5, shouldn't print 5 twice!
"""
print("TEST 1")
t1node1 = GraphNode(1)
t1node2 = GraphNode(2)
t1node3 = GraphNode(3)
t1node4 = GraphNode(4)
t1node5 = GraphNode(5)
t1node1.neighbours = [t1node2, t1node3, t1node4]
t1node2.neighbours = [t1node1]
t1node3.neighbours = [t1node1, t1node5]
t1node4.neighbours = [t1node1, t1node5]
t1node5.neighbours = [t1node3, t1node4]
printGraphBFS(t1node1)
print("")

"""
1 -- 2
  \  |
     3

expected: 1, 2, 3, shouldn't print any of the other nodes again
"""
print("TEST 2")
t2node1 = GraphNode(1)
t2node2 = GraphNode(2)
t2node3 = GraphNode(3)
t2node1.neighbours = [t2node2, t2node3]
t2node2.neighbours = [t2node1, t2node3]
t2node3.neighbours = [t2node1, t2node2]
printGraphBFS(t2node1)
