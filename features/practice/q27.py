import unittest

# 125. Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    s = s.lower()

    result = ""
    
    left = 0 
    right = len(s) - 1
    
    while left < right :

        c = s[left]
        if not ((c >= 'a' and c <= 'z') or (c >= '0' and c <= '9')) : 
            left += 1
            continue
        
        d = s[right]
        if not ((d >= 'a' and d <= 'z') or (d >= '0' and d <= '9')) : 
            right -= 1
            continue
        if c != d : 
            return False

        left += 1
        right -= 1

    return True

class TestIsPalindrome(unittest.TestCase) : 
    def test_case1(self):
        self.assertEqual(isPalindrome("A man, a plan, a canal: Panama"), True)

    def test_case2(self):
        self.assertEqual(isPalindrome("race a car"), False)

    def test_case3(self):
        self.assertEqual(isPalindrome(" "), True)

    def test_case4(self):
        self.assertEqual(isPalindrome("0P"), False)

    def test_case5(self):
        self.assertEqual(isPalindrome("a"), True)

if __name__ == "__main__":
    unittest.main()