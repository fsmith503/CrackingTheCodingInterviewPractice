
def swapSpace(str):
    a = "%20"
    for index in range(len(str)):
        if str[index] == " ":
            str = str[:index] + a + str[index:]
    print(str)

swapSpace("Mr John Smith")
