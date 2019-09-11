#pg 90 implement an algoirthmm to determine if a string has all unique characters
def test(str):
    dict1  = {}
    for char in str:
        if char in dict1.keys():
            return False
        if char not in dict1.keys():
            dict1[char] = 1 
    return True
        
print(test("asdfg"))
print(test("abccdefg"))
