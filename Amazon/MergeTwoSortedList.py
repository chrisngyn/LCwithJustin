"""
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

Pseudocode:

def merge(l1, l2):
    if l1 == None and l2 == None:
        return l1
    
    if l1 == None:
        return l2

    if l2 == None:
        return l1

    if p1.val < p2.val:
        ret = p1
        p1 = p1.next
    else:
        ret = p2
        p2 = p2.next
    
    return_this = ret

    while p1 != None or p2 != None:  # at least some more nodes to go through
        if p1 == None:
            ret.next = p2
            p2 = p2.next
        
        if p2 == None:
            ret.next = p1
            p1 = p1.next
        
        if p1.val < p2.val:
            ret.next = p1
            p1 = p1.next
        else:
            ret.next = p2
            p2 = p2.next
        
        ret = ret.next

    return return_this
"""

class ListNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mergeList(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 == None and l2 == None:
        return l1

    if l1 == None:
        return l2

    if l2 == None:
        return l1

    pointer1 = l1
    pointer2 = l2

    if pointer1.val < pointer2.val:
        ret = pointer1
        pointer1 = pointer1.next
    else:
        ret = pointer2
        pointer2 = pointer2.next

    return_this = ret

    while pointer1 != None or pointer2 != None:  # more nodes to go through
        if pointer1 == None:
            dummy_node = pointer2
            pointer2 = pointer2.next
        elif pointer2 == None:
            dummy_node = pointer1
            pointer1 = pointer1.next
        elif pointer1.val < pointer2.val:
            dummy_node = pointer1
            pointer1 = pointer1.next
        else:
            dummy_node = pointer2
            pointer2 = pointer2.next

        ret.next = dummy_node
        ret = ret.next

    return return_this

    # A more elegant solution.
    # if l1 == None and l2 == None or l2 == None:
    #     return l1
    
    # if l1 == None:
    #     return l2
    
    # sentinel = ListNode(-1)
    # head = sentinel
    # p1 = l1
    # p2 = l2
    
    # while p1 != None or p2 != None:
    #     if p1 == None:
    #         head.next = p2
    #         p2 = p2.next
    #     elif p2 == None:
    #         head.next = p1
    #         p1 = p1.next
    #     elif p1.val < p2.val:
    #         head.next = p1
    #         p1 = p1.next
    #     else:
    #         head.next = p2
    #         p2 = p2.next
        
    #     head = head.next
    
    # return sentinel.next
    