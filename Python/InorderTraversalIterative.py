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
    stack = []

    while current or len(stack) > 0:
        if current != None:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            print(current.val)
            current = current.right

            
#         stack = []
#         curr = root
#         while curr or len(stack) > 0:
#             while curr:
#                 stack.append(curr)
#                 curr = curr.left
#             curr = stack.pop()
#             print(curr.val)
#             curr = curr.right
            

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

# stack = [1, 2, 3, 4, 5]
# print(stack)
# temp = stack.pop()  <-- actually removes it from the stack
# print(stack)