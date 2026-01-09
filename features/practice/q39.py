import unittest

# 228. Summary Ranges

# You are given a sorted unique integer array nums.

# A range [a,b] is the set of all integers from a to b (inclusive).

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b
 

# Example 1:

# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
# Example 2:

# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"
 

# Constraints:

# 0 <= nums.length <= 20
# -231 <= nums[i] <= 231 - 1
# All the values of nums are unique.
# nums is sorted in ascending order.

def summaryRanges(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    
    rtnArr = []

    if not nums : 
        return rtnArr

    curr = nums[0]
    s = str(curr)
    for v in nums[1:] : 

        if s == "" : 
            s = str(curr)
        
        if curr + 1 == v : 
            curr = v
        else: 
            
            if s != str(curr) :
                s = s + "->" + str(curr)
            rtnArr.append(s)
            
            s = str(v)
            curr = v
        
    
    if s!= "" : 
        rtnArr.append(s)
    if s != str(curr) : 
        rtnArr[len(rtnArr)-1] += "->" + str(curr) 
    
    return rtnArr

class TestSummaryRanges(unittest.TestCase) : 
    def test_case1(self):
        self.assertEqual(summaryRanges([0,1,2,4,5,7]), ["0->2","4->5","7"])

    def test_case2(self):
        self.assertEqual(summaryRanges([0,2,3,4,6,8,9]), ["0","2->4","6","8->9"])

if __name__ == "__main__":
    unittest.main()