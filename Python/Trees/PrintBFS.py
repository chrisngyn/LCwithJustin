# BFS is a tree / graph traversal algorithm where you visit nodes level by level
# Uses a queue. Put nodes in, pop once its out of children, repeat
# Given a tree, print its node in Breadth First Search traversal.
# Breadth First Search is generally done ITERATIVELY.
# 3, 9, 20, 15, 7

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):  # can now create a TreeNode without providing a left or a right node
        self.val = val
        self.left = left
        self.right = right


def printBFS(root: TreeNode):
    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        current_node = queue.popleft()
        print(current_node.val)

        if current_node.left != None:
            queue.append(current_node.left)
        
        if current_node.right != None:
            queue.append(current_node.right)


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
printBFS(root)
