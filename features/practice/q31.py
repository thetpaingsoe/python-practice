import unittest

# 6. Zigzag Conversion

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000

def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    
    if numRows == 1 or len(s) <= 1: 
        return s

    result = { i : "" for i in range(numRows)}
    
    i = -1
    direction = 1
    for c in s : 
        i += direction
        result[i] += c
        
        if i == numRows - 1 :
            direction = -1
        elif i == 0 : 
            direction = 1
    
    data = ""
    for i in range(numRows) :
        data += result[i]

    return data
        
class TestConvert(unittest.TestCase) : 
    def test_case1(self):
        self.assertEqual(convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")

    def test_case2(self):
        self.assertEqual(convert("PAYPALISHIRING", 4), "PINALSIGYAHRPI")

    def test_case3(self):
        self.assertEqual(convert("A", 1), "A")

    def test_case4(self):
        self.assertEqual(convert("AB", 1), "AB")

if __name__ == "__main__":
    unittest.main()
    