"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]


"""

from collections import deque
from typing import List

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    

def binaryTreeZigZag(root: TreeNode) -> List[List[int]]:
    if root == None:
        return []

    ret = []
    queue = deque([root])
    flag = True  # when true add normally, when false add reversed

    while len(queue) > 0:
        number_nodes_in_level = len(queue)
        current_level = deque()
    
        for _ in range(number_nodes_in_level):  # need to use range on an integer because you need to generate the array of indices
            current_node = queue.popleft()

            if current_node.left != None:
                queue.append(current_node.left)
            if current_node.right != None:
                queue.append(current_node.right)
            
            if flag:
                current_level.append(current_node.val)
            else:
                current_level.appendleft(current_node.val)
        
        ret.append(list(current_level))
        flag = not flag  # OMG JUSTIN I DID IT
            
    return ret


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(binaryTreeZigZag(root))
