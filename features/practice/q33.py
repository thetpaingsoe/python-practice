import unittest

# 11. Container With Most Water

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# img : https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
 

# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

def maxArea( height):
    """
    :type height: List[int]
    :rtype: int
    """
    
    if not height : 
        return 0

    t1Index = 0
    t2Index = len(height) -1
    w = 0 

    while t1Index != t2Index : 
        if height[t1Index] < height[t2Index] : 
            
            weight = height[t1Index] * (t2Index - t1Index)
            if w < weight : 
                w = weight
            t1Index += 1
        else : 
            
            weight = height[t2Index] * (t2Index - t1Index)
            if w < weight : 
                w = weight

            t2Index -= 1

    
    return w

class TestMaxArea(unittest.TestCase) : 
    def test_case1(self):
        self.assertEqual(maxArea([1,8,6,2,5,4,8,3,7]), 49)

    def test_case2(self):
        self.assertEqual(maxArea([1,1]), 1)

if __name__ == "__main__":
    unittest.main()