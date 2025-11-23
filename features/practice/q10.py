import unittest

# 169. Majority Element

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = res = 0
        for n in nums :
            if m == 0 :
                res = n
                m += 1
            elif n == res :
                m += 1            
            else :
                m -= 1

        return res

class TestMajorityElement(unittest.TestCase):
    def test_case1(self):
        
        self.assertEqual(majorityElement([3,2,3]), 3)
    
    def test_case2(self):
        
        self.assertEqual(majorityElement([2,2,1,1,1,2,2]), 2)

    def test_case3(self):
        
        self.assertEqual(majorityElement([3,3,4]), 3)

    def test_case4(self):
        
        self.assertEqual(majorityElement([6,5,5]), 5)

if __name__ == "__main__":
    unittest.main()