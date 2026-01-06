import unittest

# 21. Merge Two Sorted Lists

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Example 1:

# https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    
    node = None
    head = None
    l1 = list1
    l2 = list2
    
    while True :
        if l1 == None and l2 == None : 
            break
        elif l1 == None : 
            if node == None :  
                node = l2
                head = node
            else : 
                node.next = l2
                node = node.next
            l2 = l2.next
        
        elif l2 == None :
            if node == None :  
                node = l1
                head = node
            else : 
                node.next = l1
                node = node.next
            l1 = l1.next

        else :
            if l1.val > l2.val :
                if node == None :  
                    node = l2
                    head = node
                else : 
                    node.next = l2
                    node = node.next
                l2 = l2.next
            else : 
                if node == None :  
                    node = l1
                    head = node
                else : 
                    node.next = l1
                    node = node.next
                l1 = l1.next
                


    return head