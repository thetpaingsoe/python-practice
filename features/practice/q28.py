import unittest

# 383. Ransom Note

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true
 

# Constraints:

# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.

def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    
    countMap = {}
    
    for m in magazine : 
        if m in countMap : 
            countMap[m] += 1
        else :
            countMap[m] = 1
    
    for r in ransomNote : 
        if r in countMap : 
            countMap[r] -= 1  

            if countMap[r] < 0 : 
                return False 

        else : 
            return False  
            
    
    return True

class TestCanConstruct(unittest.TestCase) : 
    def test_case1(self):
        self.assertEqual(canConstruct("a", "b"), False)

    def test_case2(self):
        self.assertEqual(canConstruct("aa", "ab"), False)

    def test_case3(self):
        self.assertEqual(canConstruct("aa", "aab"), True)

    def test_case4(self):
        self.assertEqual(canConstruct("aab", "baa"), True)

    def test_case5(self):
        self.assertEqual(canConstruct("bg","efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"), True)

if __name__ == "__main__":
    unittest.main()