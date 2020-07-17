"""
Write an algorithm to determine if a number 'n' is happy

A happy number is a number defined by the following process:
    starting with any positive integer,
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

public class HappyNumber {
    public static boolean isHappy(int n) {
        return true;
    }

    public static void main(String[] args) {
        System.out.println(isHappy(19)); // 'True'
        System.out.println(isHappy(20)); // 'False'
    }
}