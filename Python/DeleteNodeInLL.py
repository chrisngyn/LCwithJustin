"""
Write a function to delete a node (except the tail) in a 
singly linked list, given only access to that node.
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, 
the linked list should become 4 -> 1 -> 9 after calling 
your function.
"""

from PrintLinkedList import printLL

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def deleteNode(head, node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    node.val = node.next.val
    node.next = node.next.next
    return


head = ListNode(1)
node_to_be_deleted = ListNode(0)
dummy = head

i = 1
while i < 5:
    new_node = ListNode(i + 1)

    if i == 3:  # will delete 4 tho
        node_to_be_deleted = new_node

    dummy.next = new_node
    dummy = dummy.next
    i += 1

printLL(head)
print('--------------------------------------------------')
deleteNode(head, node_to_be_deleted)
printLL(head)