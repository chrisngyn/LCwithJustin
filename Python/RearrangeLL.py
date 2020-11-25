"""
in: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> 14 -> None

out: 2 -> 14 -> 4 -> 12 -> 6 -> 10 -> 8 -> None

find middle node

reverse from middle node

two pointers on each ends of the list

add and increment forward
"""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def reorder(head):
  head_ref = head

  middle_node = middle(head)
  first_head = head.next
  second_head = reverse(middle_node)

  while True:
    head.next = second_head
    head = head.next

    second_head = second_head.next
    if second_head == None:
      break

    head.next = first_head
    head = head.next

    first_head = first_head.next
    if first_head == None:
      break
  
  head.next = None
  return head_ref


def middle(head):
  slow, fast = head, head

  while fast != None and fast.next != None:
    slow = slow.next
    fast = fast.next.next

  return slow


def reverse(head):
  prev = None

  while head:
    next = head.next
    head.next = prev
    prev = head
    head = next
  
  return prev
