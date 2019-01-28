"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
"""

from pdb import set_trace

def same_keypress(string_one, string_two):
    ptr_1 = len(string_one) - 1
    ptr_2 = len(string_two) - 1
    
    def helper(string, ptr):
        # Compute backspace
        start = ptr
        backspace = 0
        while start >= 0:
            if string[start] == "*":
                backspace += 1
            elif backspace:
                backspace -= 1
            else:
                break
            start -= 1            
        
        return start

    while ptr_1>=0 or ptr_2>=0:
        # Determine jump for str1
        ptr_1 = helper(string_one, ptr_1)
        # Determine jump for str2
        ptr_2 = helper(string_two, ptr_2)
        # The the pointers are non-negative...
        if ptr_1 >= 0 and ptr_2 >= 0:
            # If mismatch, return False
            if string_one[ptr_1] != string_two[ptr_2]:
                return False
        # if only one of the pointers are negative, return False
        if (ptr_1 >= 0) ^ (ptr_2 >= 0):
            return False

        ptr_1 -= 1
        ptr_2 -= 1

    return True

if __name__ == "__main__":
    assert same_keypress('abcd**', 'ab') ==  True
    assert same_keypress('**abc', 'ab') ==  False
    assert same_keypress('**ab', 'ab') ==  True
    assert same_keypress('aa*b**c', 'c') ==  True
    assert same_keypress('abc***', '') ==  True
    assert same_keypress('', '') ==  True
    assert same_keypress('abc', 'abc') ==  True
    assert same_keypress('abc', 'cba') ==  False
    assert same_keypress('abc**', 'cba') ==  False
    assert same_keypress('a*b*c*', 'c*b*a*') ==  True
    assert same_keypress('a****bc*', 'b') ==  True
