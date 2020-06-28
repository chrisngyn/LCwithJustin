class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def middleNode(head: ListNode) -> ListNode:
    fast = head
    slow = head

    while fast != None:  # drawing in paint helps GG
        if fast.next is None:  # or 'while fast != None and fast.next != None'
            return slow.val

        slow = slow.next
        fast = fast.next.next
    
    return slow.val


test_head = ListNode(1)
dummy = test_head
x = 1

while x < 5:
    new_node = ListNode(x + 1)
    dummy.next = new_node
    dummy = dummy.next
    x += 1

print(middleNode(test_head))