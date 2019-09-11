#pg 91. assume you have a method isSubstring which checks if one word is a substring of another. Given two string, s1 and s2, write code to check if  s2 is a rotation of s1 using
#only one call to isSubstring


def checker(str1, str2):
    for letters in str2:
        if letters not in str1:
            print(False)
            return
    print(True)
    return 
        
checker("cat","tac")
checker("cat","hat")

