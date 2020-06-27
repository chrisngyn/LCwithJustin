"""
Write an algorithm to determine if a number 'n' is happy

A happy number is a number defined by the following process:
    Starting with any positive integer,
    replace the number by the sum of the squares of its digits,
    repeat the process until the number equals 1 (where it will stay),
    or it loops endlessly in a cycle which does not include 1

12 --> (1)^2 + (2)^2
new number --> 5

5 --> (5)^2
new number --> 25

19
1 + 81
82
64 + 4
68
36 + 64
100
1

12 -> 5 -> 25 -> 29 -> 85 -> 89 -> 136 -> 46 -> 52 -> 29
"""

def isHappy(n: int) -> bool:
    # seen_numbers = set()

    # while True:
    #     new_num = squareDigits(n)
        
    #     if new_num == 1:
    #         return True

    #     if new_num in seen_numbers:
    #         return False
    #     else:
    #         seen_numbers.add(new_num)
    #         n = new_num
    
    # return False

    slow_num = n
    fast_num = n

    while slow_num != 1 and fast_num != 1:  # if this condition breaks, we found a happy number!
        slow_num = squareDigits(slow_num)
        fast_num = squareDigits(squareDigits(fast_num))

        if slow_num == 1 or fast_num == 1:
            return True

        if slow_num == fast_num:
            return False
        
    return True


def squareDigits(n: int) -> int:
    ret = 0
    current_num = n

    while current_num != 0:
        ret += (current_num % 10) ** 2  # two astericks for powers
        current_num = current_num // 10  # two slashes for INTEGER division
    
    return ret


print(isHappy(12))
print(isHappy(19))
print(isHappy(10))