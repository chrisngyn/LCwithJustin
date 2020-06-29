"""
Reverse a singly linked list.

1 -> 2 -> 3 -> 4 -> 5 -> Null

prev = Null (Null)
current = head (1)
next = current.next (2)

while current:
    current.next = prev
    prev = current
    current = next
    next = next.next

prev = current
current = next
current.next = prev
next = next.next

5 -> 4 -> 3 -> 2 -> 1 -> Null
"""

from PrintLinkedList import printLL


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def ReverseList(head: ListNode) -> ListNode:
    # ME
    # prev = None
    # curr = head
    # next_node = curr.next

    # while curr:
    #     curr.next = prev
    #     prev = curr
    #     curr = next_node
    #     next_node = next_node.next
    
    # printLL(curr)

    # JUSTIN
    # prev = None
    # curr = head

    # while curr:
    #     next_node = curr.next
    #     curr.next = prev
    #     prev = curr
    #     curr = next_node
    
    # printLL(prev)

    prev = None
    current = head
    next = head.next # 1 2 3 4 5
    # prev is None -> None
    # current is 1 -> 2
    # next is 2 -> 3

    # 1 -> None
    # previous is now 1 -> None
    # current is 1, now it's 2 -> 3
    # next is 2, now it's 3 -> 4

    # 2 -> 1 -> None
    # current was 2, now it's 3
    # next was 3, now it's 4

    # current is 3 -> 4, 3 -> 2
    # prev was 2 now it's 3
    # current is now next 3 --> 4
    # next is 4, now its 5

    # 

    while next:
        current.next = prev 
        prev = current
        current = next
        next = next.next

    printLL(current)


test_head = ListNode(1)
dummy = test_head
x = 1

while x < 5:
    new_node = ListNode(x + 1)
    dummy.next = new_node
    dummy = dummy.next
    x += 1

# printLL(test_head)
ReverseList(test_head)