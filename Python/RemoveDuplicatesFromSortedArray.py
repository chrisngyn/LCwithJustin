"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.

Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
"""

# def removeDupesFromArray(arr) -> int:
#     ret = 1
#     last_seen = arr[0]

#     for num in arr:
#         if num == last_seen:
#             pass
#         else:
#             last_seen = num
#             ret += 1
    
#     return ret

def removeDupesFromArray(arr) -> int:
    if len(arr) == 0:
        return 0
    
    pointer = 1  # points to next index to fill
    last_seen = arr[0]

    for num in arr:
        if num != last_seen:
            arr[pointer] = num
            last_seen = num
            pointer += 1
    
    return pointer


t1 = [1, 1, 2]
newLength = removeDupesFromArray(t1)  # expect 2
print([t1[i] for i in range(newLength)])

t2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDupesFromArray(t2))  # expect 5

print(removeDupesFromArray([2, 3, 3, 3, 6, 9, 9]))  # 4
print(removeDupesFromArray([2, 2, 2, 11]))  # 2
