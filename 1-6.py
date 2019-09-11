#page 91 1.6 basic string compression using counts of repeated characters
#aabcccccaaa would become a2b1c5a3
def comp(str1):
    if len(str1) == 1:
        result = ""
        running_count = 1
        temp_char = str1[0]
        result += temp_char
        result += str(1)
        return result
    result = ""
    running_count = 1
    temp_char = str1[0]
    for i in range(1, len(str1), 1):
        if str1[i] == temp_char:
            running_count += 1
        if str1[i] != temp_char:
            result += temp_char
            result += str(running_count)
            temp_char = str1[i]
            running_count = 1
        if i == len(str1)-1:
            result += temp_char
            result += str(running_count)
    return result
print(comp("aabcccccaaa"))

