# DFS is a tree / graph traversal algorithm where you follow a path until you can't anymore (reach a leaf) then you backtrack and follow another path
# Uses a stack, but you don't need to actually declare a stack, you use the implicit stack trace calls!
# Given a tree, print its node in Depth First Search.
# Depth First Search is typically done RECURSIVELY.
# Pre-order, in-order, post-order are all DFS algorithms. There's just the one BFS.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def printDFS(root: TreeNode):
    if root == None:
        return
    
    print(root.val)
    printDFS(root.left)
    printDFS(root.right)


root = TreeNode(1)  # 1, 2, 4, 5, 3, 6, 7
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
printDFS(root)
