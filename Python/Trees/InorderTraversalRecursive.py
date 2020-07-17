"""
INORDER: LEFT ROOT RIGHT
"""

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(head: TreeNode):
    current = head

    if current == None:
        return

    inorderTraversal(current.left)
    print(current.val)
    inorderTraversal(current.right)


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5

inorderTraversal(node1)

my_array = []  # can functions even access this