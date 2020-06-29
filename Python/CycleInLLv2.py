"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) 
in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
Note: Do not modify the linked list. 

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

1 -> 2 -> 3 -> 4 -> 5
"""

from PrintLinkedList import printLL


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def detectCycle(head: ListNode) -> ListNode:  # find WHEN the cycle begins, not if there is a cycle or not
    seen_nodes = set()  # assuming unique values. if dupes allowed, we'd store memory addresses
    dummy = head

    while dummy:
        if dummy in seen_nodes:
            return dummy
        else:
            seen_nodes.add(dummy)
        
        dummy = dummy.next
    
    return None  # no cycle


print("Testing started")
dummy = ListNode(3)
head = dummy
dummy.next = ListNode(2)
dummy = dummy.next
cycleStart = dummy
dummy.next = ListNode(0)
dummy = dummy.next
dummy.next = ListNode(-4)
dummy = dummy.next
dummy.next = cycleStart
# printLL(head)  # 3 2 0 -4 AND -4 points to 2  # INFINITE LOOP!!

print(detectCycle(head))  # expect '2'

"""
I used a set to store the memory addresses of nodes I've seen. If I saw a node already, I know that's where the cycle begins.
O(n) time, O(n) space.

What you can do instead however, is first advance slow and fast until the meet.
Once they meet (are the same node), advance your head node and your slow node at the same time until they meet too.
That's where the cycle begins.
I don't really know why mathematically why that works, but it does!
"""