import unittest

# Limit : 15 mins
# 📝 Description: 
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
# find two numbers such that they add up to a specific target number. 
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one, 
# as an integer array [index1, index2] of length 2.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# 🔧 Function Signature:
# def two_sum(numbers: list[int], target: int) -> list[int]:

# 🧪 Example:
# Input: numbers = [2,7,11,15], target = 9  
# Output: [1,2]  
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2.

# 🔒 Constraints:
# 2 <= numbers.length <= 10^4
# -1000 <= numbers[i] <= 1000
# numbers is non-decreasing
# -1000 <= target <= 1000
# Exactly one solution exists

def two_sum(numbers: list[int], target: int) -> list[int] :
    left, right = 0, len(numbers) - 1

    while left < right :
        numSum = numbers[left] + numbers[right]

        if numSum == target :
            return [left+1, right+1]
        elif numSum < target : 
            left+=1
        else : 
            right-=1

    return []


class TestTwoSum(unittest.TestCase) : 
    def test_basic_case(self):
        self.assertEqual(two_sum([2,7,11,15], 9), [1,2])

    def test_basic_negative(self):
        self.assertEqual(two_sum([-5,-3,1,2,5,7], -2), [2,3])
    
    def test_basic_invalid_target(self):
        self.assertEqual(two_sum([-5,-3,1,2,5,7], 200), [])

if __name__ == "__main__":
    unittest.main()
