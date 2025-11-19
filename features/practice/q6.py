import unittest

def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """

    left = 0
    right = 0

    for i in range(m + n) :
        
        if n == 0 :
            break    
        elif nums1[left] < nums2[right] and left < m: 
            left+=1
        else :
            nums1.insert(i, nums2[right])
            nums1.pop()
            
            right += 1
            left += 1
            m += 1
            if right >= len(nums2) :
                break

    return nums1

class TestPalindromeIndex(unittest.TestCase):
    def test_case1(self):
        
        self.assertEqual(merge([1,2,3,0,0,0], 3, [2,5,6], 3), [1,2,2,3,5,6])

    def test_case2(self):
        
        self.assertEqual(merge([1], 1, [], 0), [1])

    def test_case3(self):
        
        self.assertEqual(merge([0], 0, [1], 1), [1])

    def test_case4(self):
        
        self.assertEqual(merge([2,0], 1, [1], 1), [1,2])

    def test_case5(self):
        
        self.assertEqual(merge([4,5,6,0,0,0], 3, [1,2,3], 3), [1,2,3,4,5,6])

if __name__ == "__main__":
    unittest.main()