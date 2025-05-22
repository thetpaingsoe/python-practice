# 🧩 Question: Longest Substring Without Repeating Characters
# Difficulty: Medium
# Time Limit: ⏱️ 20 minutes

# 📝 Description:
# Given a string s, find the length of the longest substring without repeating characters.

# 🔧 Function Signature:
# def length_of_longest_substring(s: str) -> int:

# 🧪 Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# 🧪 Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# 🧪 Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.

# 🔒 Constraints:
# 0 <= len(s) <= 50000
# s consists of English letters, digits, symbols, and spaces.



import unittest

def length_of_longest_substring(s: str) -> int:

    seen_chars = set()
    left = 0
    max_count = 0
    for right in range(len(s)) : 
        while s[right] in seen_chars : 
            seen_chars.remove(s[left])
            left += 1
        seen_chars.add(s[right])
        max_count = max(max_count, len(seen_chars))
    
    return max_count


class TestLongestSubString(unittest.TestCase) :

    # testing abcabcbb = 3
    def test_normal_case1(self):
        self.assertEqual(length_of_longest_substring("abcabcbb"), 3)

    # testing bbbbb = 1
    def test_normal_case2(self):
        self.assertEqual(length_of_longest_substring("bbbbb"), 1)

    # testing pwwkew = 3
    def test_normal_case3(self):
        self.assertEqual(length_of_longest_substring("pwwkew"), 3)

    # testing abba = 2
    def test_normal_case4(self):
        self.assertEqual(length_of_longest_substring("abba"), 2)

    # testing dvdf = 3
    def test_normal_case5(self):
        self.assertEqual(length_of_longest_substring("dvdf"), 3)

if __name__ == "__main__":
    unittest.main()    