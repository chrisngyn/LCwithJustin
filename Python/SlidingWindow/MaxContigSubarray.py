"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

arr: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
output: 6
explanation: [4, -1, 2, 1] has the largest sum of 6
"""

def maxSubArrayBrute(arr) -> int:
    # generate every single subarray and check which value is best
    ret, sum = 0, 0

    for i in range(len(arr)):  # [0, 1, 2, 3, 4, 5, 5, 6, 7, 8]
        sum = arr[i]
        ret = max(ret, sum)

        # range(len(arr)) --> [0, 1, 2, 3, 4, 5, 6, 7, 8]
        # range(0, len(arr)) --> [0, 1, 2, 3, 4, 5, 6, 7, 8]
        # range(1, len(arr)) --> [1, 2, 3, 4, 5, 6, 7, 8]
        for j in range(i + 1, len(arr)):  # [1, 2, 3, 4, 5, 6, 7]
            sum += arr[j]
            ret = max(ret, sum)
    
    return ret


def maxSubArrayOptimal(arr) -> int:
    # sliding window (?) / Kadane's algorithm
    ret = arr[0]
    current = arr[0]

    for num in range(1, len(arr)):
        if (current + arr[num] > arr[num]):  # constantly ask 'is it better to start a new array, or include the next val in our return array'
            current += arr[num]
        else:
            current = arr[num]
        
        ret = max(ret, current)
    
    return ret


# print(range(len(t1)))  # range(0, 9), [0, 9), [0, 8]
# print(range(0, len(t1)))  # range(0, 9) again
# print(range(1, len(t1)))  # range(1, 9), [1, 9), [1, 8]
test_arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # length 9, generating a range would give you [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(maxSubArrayBrute(test_arr))
print(maxSubArrayOptimal(test_arr))