import unittest

#14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 
# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """

    if not strs : 
        return ""

    prefix = strs[0]

    for s in strs[1:] : 
        while not s.startswith(prefix) and prefix : 
            prefix = prefix[:-1]
        
        if not prefix : 
            return ""

    return prefix

class TestLongestCommonPrefix(unittest.TestCase) : 
    def test_case1(self):
        self.assertEqual(longestCommonPrefix(["flower","flow","flight"]), "fl")

    def test_case2(self):
        self.assertEqual(longestCommonPrefix(["dog","racecar","car"]), "")

    def test_case3(self):
        self.assertEqual(longestCommonPrefix(["a"]), "a")

    def test_case4(self):
        self.assertEqual(longestCommonPrefix(["ab", "a"]), "a")
    
if __name__ == "__main__":
    unittest.main()