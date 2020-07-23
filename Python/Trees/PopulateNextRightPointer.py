# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None, pointer = None):
        self.val = val
        self.left = left
        self.right = right
        self.pointer = pointer


def PopulatingNextRightPointers(root: TreeNode) -> TreeNode:  # after assigning all the 'pointer' fields of the nodes, return the root
    if root == None:  # edge case check
        return root

    queue = deque([root])

    while len(queue) > 0:
        num_nodes_in_level = len(queue)
        last_node = None

        for _ in range(num_nodes_in_level):
            curr_node = queue.popleft()

            if curr_node.right != None:
                queue.append(curr_node.right)
            
            if curr_node.left != None:
                queue.append(curr_node.left)
            
            curr_node.next = last_node
            last_node = curr_node
    
    return root


def print_level_order(self):
    nextLevelRoot = self
    while nextLevelRoot:
        current = nextLevelRoot
        nextLevelRoot = None
        while current:
            print(str(current.val) + " ", end='')
            if not nextLevelRoot:
                if current.left:
                    nextLevelRoot = current.left
                elif current.right:
                    nextLevelRoot = current.right
            current = current.next
        print()


# expected;
# 12
# 7 1
# 9 10 5

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

PopulatingNextRightPointers(root)

print("Level order traversal using 'next' pointer: ")
print_level_order(root)
