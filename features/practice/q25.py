import unittest

# 151. Reverse Words in a String

# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

# Constraints:

# 1 <= s.length <= 104
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.

def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    charArr = s.split(" ")
    result = ""

    for i in range(len(charArr) -1, -1, -1) :
        if charArr[i] : 
            result += charArr[i] + " "                
        
    return result[0:len(result)-1]

class TestReverseWords(unittest.TestCase) : 
    def test_case1(self):
        self.assertEqual(reverseWords("the sky is blue"), "blue is sky the")

    def test_case2(self):
        self.assertEqual(reverseWords("  hello world  "), "world hello")

    def test_case3(self):
        self.assertEqual(reverseWords("a good   example"), "example good a")
    
if __name__ == "__main__":
    unittest.main()