import unittest

# 135. Candy

# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.

# Example 1:

# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
# Example 2:

# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two conditions.
 

# Constraints:

# n == ratings.length
# 1 <= n <= 2 * 104
# 0 <= ratings[i] <= 2 * 104

def candy(ratings):
    """
    :type ratings: List[int]
    :rtype: int
    """

    minNum = len(ratings)
    
    leftArr = [0] * len(ratings)
    prev = 0
    counter = 1
    for i in range(len(ratings)) :
        
        if i == 0 : 
            leftArr[i] = 0                
        else : 
            if prev < ratings[i] : 
                
                leftArr[i] += counter
                counter += 1
            else : 
                counter = 1

        prev = ratings[i]
    
    rightArr = [0] * len(ratings)
    counter = 1
    for i in range(len(ratings) -1, -1, -1) :
        
        if i == len(ratings) -1  : 
            rightArr[i] = 0                
        else : 
            if prev < ratings[i] : 
                
                rightArr[i] += counter
                counter += 1
                
            else : 
                counter = 1
        prev = ratings[i]

        if(rightArr[i] > leftArr[i]) : 
            minNum += rightArr[i]
        else :
            minNum += leftArr[i]

    return minNum


class TestCandy(unittest.TestCase) : 
    def test_case1(self):
        self.assertEqual(candy([1,0,2]), 5)

    def test_case2(self):
        self.assertEqual(candy([1,2,2]), 4)
    
if __name__ == "__main__":
    unittest.main()
