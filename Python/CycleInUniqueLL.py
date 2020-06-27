"""
Given a n-sized linked list determine if there's a cycle in it
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    

def hasCycle(head: ListNode) -> bool:
    seen_nodes = set()
    temp = head

    while temp:
        if temp.val in seen_nodes:
            return True
        else:
            seen_nodes.add(temp.val)
        
        temp = temp.next
    
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