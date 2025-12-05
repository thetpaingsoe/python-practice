import unittest

# 58. Length of Last Word

# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.

def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """

    words = s.split(' ')
    for i in range(len(words) -1 , -1, -1) : 
        if len(words[i]) > 0 and words[i][0] != ' ' : 
            return len(words[i])

class TestLengthOfLastWord(unittest.TestCase) : 
    def test_case1(self):
        self.assertEqual(lengthOfLastWord("Hello World"), 5)

    def test_case2(self):
        self.assertEqual(lengthOfLastWord("   fly me   to   the moon  "), 4)
    
    def test_case3(self):
        self.assertEqual(lengthOfLastWord("luffy is still joyboy"), 6)

if __name__ == "__main__":
    unittest.main()
