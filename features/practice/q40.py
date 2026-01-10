import unittest

# 67. Add Binary.

# Given two binary strings a and b, return their sum as a binary string.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    
    return format(int(a, 2) + int(b, 2), 'b')

class TestAddBinary(unittest.TestCase) : 
    def test_case1(self):
        self.assertEqual(addBinary("11", "1"), "100")

    def test_case2(self):
        self.assertEqual(addBinary("1010","1011"), "10101")

    def test_case3(self):
        self.assertEqual(addBinary("1111","1111"), "11110")

if __name__ == "__main__":
    unittest.main()