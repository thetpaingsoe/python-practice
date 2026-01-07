import unittest

# 2. Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:

# https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

def addTwoNumbers(self, l1, l2):
    """
    :type l1: Optional[ListNode]
    :type l2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    
    n1 = ""
    n2 = ""

    while l1 != None : 
        n1 =  str(l1.val) + n1
        l1 = l1.next

    while l2 != None : 
        n2 = str(l2.val) + n2
        l2 = l2.next

    resStr = str(int(n1) + int(n2))[::-1]
    res = ListNode(int(resStr[0]), None)
    resHead = res
    for v in resStr[1:]: 
        res.next = ListNode(int(v), None)
        res = res.next

    return resHead