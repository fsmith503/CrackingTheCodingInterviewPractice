#page 91, 1.8
#write algorithm such that if an element in an M x N matrix is 0, its entire row and column are set to 0.

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

