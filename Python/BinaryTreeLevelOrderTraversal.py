"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

    3
   / \
  9  20
    /  \
   15   7

Given binary tree [3, 9, 20, null, null, 15, 7], return,
[
  [3],
  [9,20],
  [15,7]
]

tl;dr - I need to do BFS (breadth first search).

Breadth first search is a tree / graph traversal algorithm that allows you to visit nodes level by level.

Approach:

Use a queue. Queue 3, then queue 9, then 20, once 3 has no more children nodes to 'visit' we'll deque 3 and repeat with 9 and 20.


from collections import deque
def BFS(root):
    ret = []
    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        node = queue[0]
        length = len(queue)
        ret.append([i.val for i in queue])  <-- LIST COMPREHENSION

alt:    row = []
        for i in queue:
            row.append(i.val)
        ret.append(row)

        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)

        for num in range(length):
            queue.popleft()
"""


from collections import deque
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: TreeNode) -> List[List[int]]:
    ret = []
    queue = deque([root])  # double ended queue

    while len(queue) > 0:
        ret.append(queue)  #
        current_node = queue.popleft()


    # return ret
root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
levelOrder(root)