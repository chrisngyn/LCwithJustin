"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

alt approach: traverse the string backwards. if we see a '#' keep a counter 'num_ignore' of the next number of characters to ignore
"""

def backspaceStringCompare(S, T) -> bool:
    s1 = []
    s2 = []

    for char in S:  # O(n)
        if char == '#' and len(s1) != 0:
            s1.pop()
        else:
            s1.append(char)

    for char in T:  # O(m)
        if char == '#' and len(s2) != 0:
            s2.pop()
        else:
            s2.append(char)

    ret1 = "".join(s1)  # O(n)
    ret2 = "".join(s2)  # O(m)

    return ret1 == ret2  # O(2 * (n+m)) == O(n+m) time, space is O(n+m)
