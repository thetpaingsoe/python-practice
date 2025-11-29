import unittest

# https://leetcode.com/problems/jump-game-ii

# 45. Jump Game II

# You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [2,3,0,1,4]
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 1000
# It's guaranteed that you can reach nums[n - 1].


def jump( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    ans = 0 
    fartest = 0
    end = 0
    for i in range(len(nums) -1) :
        fartest = max(fartest, i + nums[i])

        if fartest >= len(nums) -1 : 
            ans += 1
            break

        if i == end : 
            ans += 1
            end = fartest

    return ans

class TestJump(unittest.TestCase):
    def test_case1(self):
        
        self.assertEqual(jump([2,3,1,1,4]), 2)
    
    def test_case2(self):
        
        self.assertEqual(jump([2,3,0,1,4]), 2)

    def test_case3(self):
        
        self.assertEqual(jump([1,2]), 1)
    
    def test_case4(self):
        
        self.assertEqual(jump([1,2,3]), 2)

    def test_case5(self):
        
        self.assertEqual(jump([1,2,1,1,1]), 3)

if __name__ == "__main__":
    unittest.main()