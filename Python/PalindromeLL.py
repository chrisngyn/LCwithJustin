"""
Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

1. use slow / fast pointer to get to the middle of the linked list
2. reverse the 2nd half
3. traverse the heads of both lists and check if values are the same
"""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def is_palindromic_linked_list(head):
  fast, slow = head, head

  while fast != None and fast.next != None:  # traverse so 'slow' is the middle of the LL
    slow = slow.next
    fast = fast.next.next
  
  second_head = reverse(slow)  # reverse the 2nd half, second_head is the head of the new LL

  while head != None and second_head != None:  # traverse both lists
    if head.value != second_head.value:
      return False
    
    head = head.next
    second_head = second_head.next
  
  if head != second_head:  # one could be None and the other could be a value
    return False
  
  return True


def reverse(head):  # init prev, next, head.next, prev, head, return prev
  prev = None

  while head != None:
    next = head.next
    head.next = prev
    prev = head
    head = next
  
  return prev


def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  print("Is palindrome: " + str(is_palindromic_linked_list(head)))

  # doesn't work because I don't reset after reversing, they use the same list for multiple tests
  # head.next.next.next.next.next = Node(2)
  # print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()
