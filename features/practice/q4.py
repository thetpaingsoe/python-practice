import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:

    tail = ListNode(-1)
    dummy = tail
    
    while list1 and list2 :
        if list1.val <= list2.val :
            tail.next = list1
            list1 = list1.next            
        else :
            tail.next = list2
            list2 = list2.next
        tail = tail.next
        
    tail.next = list1 if list1 else list2

    return dummy.next


def parseNodeToString(node : ListNode) :
    if node is None :
        return None 

    result = ""
    while node :
        result += f"{node.val},"
        node = node.next

    return result

class TestMergeTwoLists(unittest.TestCase):
    def test_case1(self):
        node3 = ListNode(3)
        node2 = ListNode(2, node3)
        node1 = ListNode(1, node2)
        
        node6 = ListNode(3)
        node5 = ListNode(2, node6)
        node4 = ListNode(1, node5)
        
        self.assertEqual(parseNodeToString(mergeTwoLists(node1, node4)), "1,1,2,2,3,3,")


    def test_case2(self):
        node3 = ListNode(4)
        node2 = ListNode(2, node3)
        node1 = ListNode(1, node2)
        
        node6 = ListNode(4)
        node5 = ListNode(3, node6)
        node4 = ListNode(1, node5)
        
        self.assertEqual(parseNodeToString(mergeTwoLists(node1, node4)), "1,1,2,3,4,4,")

    def test_case3(self):
        
        self.assertEqual(parseNodeToString(mergeTwoLists(None, None)), None)

    def test_case4(self):
        node1 = ListNode(0)
        
        self.assertEqual(parseNodeToString(mergeTwoLists(node1, None)), "0,")
        

if __name__ == "__main__":
    unittest.main()