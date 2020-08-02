"""
Merge K sorted singly linked lists.

Input: list of head nodes
Output: head reference to one sorted list

Approach 1:
loop through all of the head nodes and append all the values to an array O(n) and O(n) space
sort the array O(nlogn)
loop through the sorted array, create a new ListNode for each value and stitch it together O(n) time and O(n) more space

Approach 2:
what if we loop through our list of head nodes? and each time, we just find the smallest value of all the head values
then append the head val, and advance it, rinse and repeat until all nodes are gone

this is a good approach, here's the problem though, how do you find the minimum value of a level?
i was originally going to say loop through the level of nodes (size K for K lists) to find the minimum
then loop through it AGAIN and if it == to the minimum, then you know to advance it O(K) AGAIN

so finding the minimum of each level everytime is kind of cancer. looping through an array twice to find a minimum value

but look at what we're trying to do - find the minimum element each time. does that make you think of anything?

boy i sure hope it does. MINIMUM HEAP!

time complexity - O(n log k)
space complexity - O(k) - size of the array is always num of lists we have (bc there's that many num of head pointers)
"""

from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

def mergeLists(lists: List[ListNode]) -> ListNode:  # approach 1 - the 'simple' approach, not the most optimal (approach 2 is)
    nodes = []
    sentinel = ListNode(-1)
    dummy = sentinel

    for head in lists:  # for all the nodes, in all K lists, add the values to our array (O(n), O(n) space)
        while head != None:
            nodes.append(head.val)
            head = head.next

    nodes.sort()  # sort the array (O(nlogn))
            
    for node in nodes:  # for all the values in our array, create a new ListNode, stitch it together (O(n), O(n) space)
        new_node = ListNode(node)
        dummy.next = new_node
        dummy = dummy.next

    return sentinel.next
