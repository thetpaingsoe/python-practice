import unittest

# https://leetcode.com/problems/jump-game/submissions/1841774641/

# 55. Jump Game

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.


# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    g = 1
    status = True
    for i in range(len(nums) - 2, -1, -1) : 
        
        if nums[i] >= g : 
            status = True
            g = 1
        else : 
            status = False
            g += 1

    return status

class TestCanJump(unittest.TestCase):
    def test_case1(self):
        
        self.assertEqual(canJump([2,3,1,1,4]), True)
    
    def test_case2(self):
        
        self.assertEqual(canJump([3,2,1,0,4]), False)

if __name__ == "__main__":
    unittest.main()