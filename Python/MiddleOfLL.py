# Given a non-empty, singly linked list with head node head, return a middle node of linked list.
# If there are two middle nodes, return the second middle node.
# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

from PrintLinkedList import printLL

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def middleNode(head: ListNode) -> ListNode:
    ret = head
    dummy = head
    length = 0

    while dummy != None:
        length += 1
        dummy = dummy.next
        
    mid = (length // 2) + 1

    # i = 0
    # while i < mid - 1
    #     i += 1
    #     ret = ret.next

    for i in range(mid - 1):  # mid = 3, range is an array of [0, 1, 2]
        ret = ret.next

    return ret.val


test_head = ListNode(1)
dummy = test_head
x = 1

while x < 5:
    new_node = ListNode(x + 1)
    dummy.next = new_node
    dummy = dummy.next
    x += 1

# printLL(test_head)
print(middleNode(test_head))