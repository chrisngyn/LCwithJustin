class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def make_five_nodes_and_print_val():
    dummy = Node(1)
    head = dummy

    i = 1
    while i <= 5:
        print(dummy.val)
        new_node = Node(i + 1)
        dummy.next = new_node
        dummy = dummy.next
        i += 1

make_five_nodes_and_print_val()