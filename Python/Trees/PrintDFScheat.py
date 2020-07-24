from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def printDFS(root: TreeNode):  # when you want a function with different arguments, make a new method and pass the whole fucking thing over lmao
    if root == None:           # Justin wanted me to put it all in an array and print but without modifying the original method. so make a helper function with modified params lol
        return []

    ret = []
    return cheat_method(root, ret)

    
def cheat_method(root: TreeNode, arr: List) -> List:
    if root == None:
        return
    
    arr.append(root.val)
    cheat_method(root.left, arr)
    cheat_method(root.right, arr)
    
    return arr


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print(printDFS(root))
