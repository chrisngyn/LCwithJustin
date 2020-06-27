"""
Given a n-sized linked list determine if there's a cycle in it

Use the tortise and hare pattern
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    

def hasCycle(head: ListNode) -> bool:
    fast = head
    slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if (slow == fast):
            return True

    return False


head = ListNode(1)
temp = head

i = 1
while i < 5:
    dummy_node = ListNode(i + 1)
    temp.next = dummy_node
    temp = temp.next
    i += 1

print(hasCycle(head))  # False

cycle_node = ListNode(10)
temp.next = cycle_node
cycle_node.next = head

print(hasCycle(head))  # True