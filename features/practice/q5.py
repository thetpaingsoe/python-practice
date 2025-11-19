import unittest

def palindromeIndex(s):

    baseIndex = -1
    baseChar = None

    chars = {}

    currentChar = None

    isFound = False


    for i, char in enumerate(s) : 
        if currentChar is None : 
            currentChar = char
            if not char in chars.keys() : 
                chars[char] = 1
        else : 
            if currentChar != char : 
                
                if isFound : 
                    baseChar = char
                    baseIndex = i
                    break
                else : 
                    baseChar = currentChar
                    baseIndex = i - 1
                    
            if not char in chars.keys() : 
                chars[char] = 1
            else :
                chars[char] += 1
            if chars[char] > 1 :
                if baseChar != char and baseChar is not None and currentChar != baseChar: 
                    break
                else : 
                    isFound = True

            currentChar = char

    return baseIndex


class TestPalindromeIndex(unittest.TestCase):
    def test_case1(self):
        
        self.assertEqual(palindromeIndex("aaab"), 3)


    def test_case2(self):
        
        self.assertEqual(palindromeIndex("baaa"), 0)

    def test_case3(self):
        
        self.assertEqual(palindromeIndex("aaa"), -1)

    def test_case4(self):
        
        self.assertEqual(palindromeIndex("bcbc"), 3)
        

if __name__ == "__main__":
    unittest.main()