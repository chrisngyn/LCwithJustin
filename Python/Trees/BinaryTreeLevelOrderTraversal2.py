"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example, given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]
"""

from collections import deque
from typing import List

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def levelOrderBottom(root: TreeNode) -> List[List[int]]:
    if root == None:
        return []

    ret = deque()
    queue = deque([root])

    while len(queue) > 0:
        current_level = []
        num_nodes_in_next_level = len(queue)  # this will get the number of nodes that belong in the level, so you'll go thru this amount getting next levels nodes

        for _ in range(num_nodes_in_next_level):  # 1, [0]
            node = queue.popleft()
            print("Current node value:", node.val)

            if node.left != None:
                queue.append(node.left)
            
            if node.right != None:
                queue.append(node.right)

            current_level.append(node.val)
        
        ret.appendleft(current_level)  # better than ret being an array, and doing ret.insert(0, current_level) (which is O(n), this is O(1))

    return ret
    

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print(str(levelOrderBottom(root)))

root2 = TreeNode(3)
root2.left = TreeNode(9)
root2.right = TreeNode(20)
root2.right.left = TreeNode(15)
root2.right.right = TreeNode(7)
print(str(levelOrderBottom(root2)))
