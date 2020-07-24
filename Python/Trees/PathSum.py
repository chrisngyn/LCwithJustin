"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.


Pseudocode

Note: instead of going down one path and having to recurse back up...what if we went down the left and right path at the same time? :thinking:

that would remove us having to keep a stack, and pushing, popping values, recalculating sum, etc.

def pathSum(root: TreeNode, sum: int) -> bool:
    if root == None:
        return False

    calculate_left = calculate_sum(root.left, sum - root.val)
    calculate_right = calculate_sum(root.right, sum - root.val)

    return False

def calculate_sum(root: TreeNode, sum: int) -> int:
    print(sum)
    if root == None:
        if sum == 0:
            return True
        else:
            return
    
    calculate_sum(root.left, sum - root.val)
    calculate_sum(root.right, sum - root.val)

Justin: "you don't need a helper function"

do I need a flag?? toggle it to true once I find a sum that is 0??
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pathSum(root: TreeNode, sum: int) -> bool:  # MUST be from ROOT to a LEAF. can't do an intermediate path. kinda dumb but whatever.
    if root == None:
        return False
    
    if root.left and root.right and sum - root.val == 0:  # if the first two conditions are true, we're at a leaf. if the third condition is true, we're at 0!
        return True  # if you have FALSE or FALSE or FALSE or TRUE or FALSE or FALSE, it'll return TRUE.
    
    return pathSum(root.left, sum - root.val) or pathSum(root.right, sum - root.val)  # while you're not at a leaf, keep recursing down the tree


# def pathSum(root: TreeNode, sum: int) -> bool:  # almost right. this has a nasty edge case. if your root is null AND the expected suim is 0, returns true when it SHOULD be false.
#     if root == None:
#         if sum == 0:
#             return True
#         return False

#     return pathSum(root.left, sum - root.val) or pathSum(root.right, sum - root.val)


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.right = TreeNode(1)
print(pathSum(root, 22))

# TL;DR - THIS PROBLEM WAS FUCKING ROUGH. WENT FROM MAKING HELPER FUNCTIONS TO USING FLAGS AND UGH
