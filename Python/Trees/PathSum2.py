"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1

Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""

from typing import List

class TreeNode():
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

def allPathSum(root: TreeNode, sum: int) -> List[List[int]]:
    if root == None:
        return []
    
    answers = []
    current = []

    if sumToLeaf(root.left, sum-root.val, current)[0] == 0:
        answers.append(sumToLeaf[1])

    if sumToLeaf(root.right, sum-root.val, current)[0] == 0:
        answers.append(sumToLeaf[1])
    
    return answers

def sumToLeaf(root, sum, arr) -> (int, list):
    if root == None:  # at leaf
        return

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)
printDFS(root)
# print(allPathSum(root))
