import unittest

def isValidBrackets(s: str) :

    stack = []
    bracket_map = {')':'(', '}':'{', ']':'['}

    for index in range(len(s)):
        
        if s[index] in bracket_map.values(): 
            stack.append(s[index])            
        elif stack[len(stack)-1] == bracket_map[s[index]]:
            stack.pop()
        else : 
            return False
        
    return not stack
    
class TestIsValidBrackets(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(isValidBrackets("()"), True)

    def test_case2(self):
        self.assertEqual(isValidBrackets("()[]{}"), True)

    def test_case3(self):
        self.assertEqual(isValidBrackets("(]"), False)
    
    def test_case4(self):
        self.assertEqual(isValidBrackets("([)]"), False)

    def test_case5(self):
        self.assertEqual(isValidBrackets("{[]}"), True)

    def test_case6(self):
        self.assertEqual(isValidBrackets("((("), False)


if __name__ == "__main__" : 
    unittest.main()