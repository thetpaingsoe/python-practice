import unittest

# 28. Find the Index of the First Occurrence in a String

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.

def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """

    if not needle in haystack : 
        return -1
    
    index = -1
    for i in range(len(haystack)) : 

        if haystack[i] == needle[0] : 
            index = i
            count = 0
            
            for j in range(len(needle)) : 
                k = i + j
                if needle[j] != haystack[k] : 
                    index = -1
                    break
                else : 
                    count += 1

            if count == len(needle) :
                return index


    return index

class TestStrStr(unittest.TestCase) : 
    def test_case1(self):
        self.assertEqual(strStr("sadbutsad", "sad"), 0)

    def test_case2(self):
        self.assertEqual(strStr("leetcode", "leeto"), -1)

    def test_case3(self):
        self.assertEqual(strStr("mississippi", "issip"), 4)
    
if __name__ == "__main__":
    unittest.main()
