class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def printLL(node):
    while node:
        print(node.val)
        node = node.next