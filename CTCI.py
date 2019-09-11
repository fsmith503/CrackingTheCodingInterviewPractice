
#pg 90 implement an algoirthmm to determine if a string has all unique characters
"""
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
"""


#pg 90 given two strings wirte a mehtod to decide if one is a permutation of the other
"""
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
"""


"""
def swapSpace(str):
    a = "%20"
    for index in range(len(str)):
        if str[index] == " ":
            str = str[:index] + a + str[index:]
    print(str)

swapSpace("Mr John Smith")
"""


#page 91, 1.8
#write algorithm such that if an element in an M x N matrix is 0, its entire row and column are set to 0.

"""
def zerod(array):
    print(array)
    hit = False
    rows = []
    cols = []
    for i in range(len(array)):
        for k in range(len(array)):
            if array[i][k] == 0:
                rows.append(i)
                cols.append(k)
    for i in range(len(array)):
        for k in range(len(array)):
            if i in rows or k in cols:
                array[i][k] = 0
    print(array)



#[[1,2,3],[2,0,3],[2,2,2]]
zerod([[1,2,3],[0,0,3],[2,2,2]])
"""


#pg 91. assume you have a method isSubstring which checks if one word is a substring of another. Given two string, s1 and s2, write code to check if  s2 is a rotation of s1 using
#only one call to isSubstring
"""

def checker(str1, str2):
    for letters in str2:
        if letters not in str1:
            print(False)
            return
    print(True)
    return 
        
checker("cat","tac")
checker("cat","hat")
"""


#page 923 linked lists
#pg 94

# CTCI 2.1

from random import randint

class Node(object):
    #Constructor
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class LinkedList(object):
    #Constructor
    def __init__(self, head = None, size = None):
        self.head = head
        self.size = size

    #Display
    def __str__(self):
        res = []
        cur = self.head
        while cur:
            res.append(str(cur.val))
            cur = cur.next
        return ' -> '.join(res)



    #Insert
    def insert_head(self, val):
        if self.head == None:
            self.head = Node(val)
        else:
            temp = Node(val) #temp Node
            temp.next = self.head  #Head
            self.head = temp #headreferenceTemp Node

    #nsert
    def insert_tail(self, val):
        if self.head == None:
            self.head = Node(val)
        else:
            cur = self.head
            temp = Node(val)
            while cur.next:  #idk
                cur = cur.next
            cur.next = temp

    #Generate Insert 10
    def generate(self):
        for _ in xrange(10):
            self.insert_tail(randint(0,9))

    #Insert
    def insert_multiple(self, val):
        for v in val:
            self.insert_tail(v)

    #Search
    def search(self, val):
        if self.head == None:
            raise ValueError("List is empty")

        cur = self.head
        while cur:
            if cur.val == val:
                return True
            else:
                cur = cur.next
        return False

    #Delete V1 using Prev
    def delete_1(self, val):
        if self.head == None:
            return self.head

        cur = self.head
        prev = None

        while cur:
            if cur.val == val:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
            prev = cur
            cur = cur.next

    #Delete V2 not using Prev
    def delete_2(self, val):
        if self.head == None:
            return self.head

        cur = self.head
        #Edge case
        if cur.val == val:
            self.head = cur.next

        #The rest
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

def remove_dups(ll, prev=None):
    head = ll.head
    cur = ll.head
    hash = {}

    while cur:
        if cur.val in hash:
            prev.next = cur.next
        else:
            hash[cur.val] = 1
        prev = cur
        cur = cur.next
    return head


# 2 Pointers (Runner Methods)
# Space complexity: O(1)
# Time complexity: O(N^2)
def remove_dups_2(ll, val):
    head = ll.head
    cur = ll.head
    runner = ll.head

    while cur:
        prev = runner
        runner = runner.next

        if runner and runner.val == cur.val:
            prev.next = runner.next
            runner = runner.next

        if runner == None:
            cur = cur.next
            runner = cur
    return head


#Some Tests:
ll = LinkedList()
ll.generate()
print(ll)
remove_dups_2(ll, 3)
print(ll)















