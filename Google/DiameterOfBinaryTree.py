"""
Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

Example:
Given a binary tree

          1
         / \
        2   3
       / \     
      4   5    

Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""

diameter = -float("inf")

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameter(root: TreeNode) -> int:
    calculateDiameter(root)
    return diameter

def calculateDiameter(root: TreeNode) -> int:
    if root == None:
        return
    
    calculateDiameter(root.left)
    calculateDiameter(root.right)

    diameter = max(diameter, ??)
    return ??