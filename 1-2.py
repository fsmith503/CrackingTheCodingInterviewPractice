#pg 90 given two strings wirte a mehtod to decide if one is a permutation of the other

def permu(str1, str2):
    for items in str1:
        if items not in str2:
            return False
    for items1 in str2:
        if items1 not in str1:
            return False
    return True

print(permu("dog","god"))
print(permu("mom","dad"))

