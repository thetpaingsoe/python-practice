import unittest

# https://leetcode.com/problems/h-index

# 274. H-Index

# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

# Example 1:

# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
# Example 2:

# Input: citations = [1,3,1]
# Output: 1
 

# Constraints:

# n == citations.length
# 1 <= n <= 5000
# 0 <= citations[i] <= 1000

def hIndex(citations):
    """
    :type citations: List[int]
    :rtype: int
    """

    citations.sort()
    citations.reverse()

    c = 0
    for i, num in enumerate(citations, 1) : 
        if num >= i : 
            c = i
        else : 
            break
    return c

class TestHIndex(unittest.TestCase):
    def test_case1(self):
        
        self.assertEqual(hIndex([3,0,6,1,5]), 3)
    
    def test_case2(self):
        
        self.assertEqual(hIndex([1,3,1]), 1)

    def test_case3(self):
        
        self.assertEqual(hIndex([100]), 1)
    
    def test_case4(self):
        
        self.assertEqual(hIndex([1,2]), 1)

    def test_case5(self):
        
        self.assertEqual(hIndex([1,2,2]), 2)

    def test_case6(self):
        
        self.assertEqual(hIndex([1,1]), 1)

    def test_case7(self):
        
        self.assertEqual(hIndex([2,2,2]), 2)

    def test_case8(self):
        
        self.assertEqual(hIndex([0]), 0)

if __name__ == "__main__":
    unittest.main()