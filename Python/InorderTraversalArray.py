"""
INORDER: LEFT ROOT RIGHT
"""

from typing import List

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(head: TreeNode, arr: List[int]) -> List[int]:  # how can I do this without a passing an array as param
    current = head

    if current == None:
        return

    inorderTraversal(current.left, arr)
    arr.append(current.val)
    inorderTraversal(current.right, arr)

    return arr


def inorderTraversalNoExtraArgs(head: TreeNode) -> List[int]:
    if not head:
        return []
    res = []

    res += inorderTraversalNoExtraArgs(head.left)
    res.append(head.val)
    res += inorderTraversalNoExtraArgs(head.right)

    return res


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5

town_bicycle = []
print(inorderTraversal(node1, arr))
print(inorderTraversalNoExtraArgs(node1))
