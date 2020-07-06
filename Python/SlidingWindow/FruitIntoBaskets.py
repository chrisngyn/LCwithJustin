"""
In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:
    1. Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
    2. Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.

Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?

Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].

Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].

Pseudocode #1:

I think you just want to find the max contiguous subarray length with at most two unique values tbh?

^^ OMG I WAS RIGHT LOL

-always add the next value into your array
-while the number of unique element in your array is > 2, pop off
-always do checks to update max, ret = max(ret, whatever)

def totalFruit(self, tree):
    ret = 0
    win_start = 0
    win_sum = 0  # end - start + 1
    num_unique = 0

    for num in tree:
        win_sum += 1

    return ret

Pseudocode #2:

use a dict?

def totalFruit(self, tree):
    ret = 0
    win_start = 0
    dic = {}

    for win_end in range(len(tree)):
        num = tree[win_end]

        if num not in dic:
            dic[num] = 0

        dic[num] += 1
        
        while len(dic) > 2:
            if dic[win_start] > 1:
                dic[win_start] -= 1
            else:
                del dic[win_start]
            
            win_start += 1
        
        ret = max(ret, win_end - win_start + 1)

    return ret
"""

from typing import List

def totalFruit(tree: List[int]) -> int:
    ret, win_start = 0, 0
    dic = {}

    for win_end in range(len(tree)):
        num = tree[win_end]

        if num not in dic:
            dic[num] = 0
        
        dic[num] += 1

        while len(dic) > 2:
            if dic[tree[win_start]] > 1:
                dic[tree[win_start]] -= 1
            else:
                del dic[tree[win_start]]
            
            win_start += 1
        
        ret = max(ret, win_end - win_start + 1)

    return ret


test_arr1 = [1, 2, 1]
print(totalFruit(test_arr1))  # 3
test_arr2 = [0, 1, 2, 2]
print(totalFruit(test_arr2))  # 3
test_arr3 = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
print(totalFruit(test_arr3))  # 5