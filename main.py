''''''

'Task 01'
# For the given matrix,  print in ascending order
# the indexes of columns with exactly two distinct values in it.
# If there is no such column, print word None.
# The output values are separated by single spaces on a single line.
'''
Example
Input
1
6 11
30 14 25 19 22 18 16 24 28 13 22
19 14 32 33 35 18 21 32 19 13 12
19 14 17 40 35 15 16 24 28 18 22
31 14 17 19 22 15 21 24 28 13 22
30 22 25 17 35 18 21 24 37 32 22
30 14 17 34 35 15 16 24 28 18 34
Output
1 4 5 6 7
'''
def task01( matrix ):
    P= list(map(list,zip(*matrix)))
    New=[]
    for i in range(len(P)):
        if len(set(P[i])) == 2:
            New.append(i)
    for k in New:
        print(k,end=' ')
    if len(New) == 0:
        print(None)


'Task 02'
# In the given matrix, find maximum of sums of all submatrices of size  2x2
# and count the number of occurrences of this maximum in the whole matrix.
# The sum of a submatrix is the sum of all its elements.
# # The size of input matrix is in range[3x3 .. 1000x1000].
# Output consists of one line with two integers separated by space:
# The maximum sum of a 2x2 submatrix of the input matrix
# and the number of occurrences of a submatrices with this sum in the input matrix.
'''
Example
Input
2
3 5
0 1 0 2 1 
1 0 2 0 1
2 1 0 0 1
Output
4 3
Comment
The maximum 2x2 sum, equal to 4, is attained at submatrices with their
upper left corners at positions [0][2], [0][3], and [1][0].
'''
def task02( matrix ):
    p=[]
    Max=0
    flag=0
    for i in range(R-1):
        for j in range(C-1):
            temp = arr2d[i][j]+arr2d[i][j+1]+arr2d[i+1][j]+arr2d[i+1][j+1]
            if temp>Max:
                Max = temp
                flag = 1
            elif temp==Max:
                flag +=1
    print(Max,flag)



'Task 03'
# For the given square matrix M, create a new matrix P,
# which dimensions are the same as the dimensions of M.
# For each non-zero value in M at position [i][j] it holds,
# that P contains the same value at position [i][j].
# For each zero value in M at position [i][j] it holds,
# that P contains at position [i][j] the sum of all values
# which are either above this zero in the same column in M
# or to the right of this zero in the same row in M.
# The size of input matrix M is in range[3x3 .. 900x900].
# If both matrix sizes are not bigger than 20, print matrix P
# in the same format as the input matrix M, do not print the
# dimensions of P.
# If the size of M is bigger than 20 x 20, print only the
# rightmost bottommost submatrix of P of size 20x20.
# In any case, print also, after the (sub)matrix, on the next line,
# the total of all values by which were the zeros substituted.
'''
对于给定的方形矩阵M，创建一个新的矩阵P，其尺寸与M的尺寸相同。
对于M中位于[i][j]位置的每个非零值，可以认为P在[i][j]位置包含相同的值。
对于M中位于[i][j]位置的每个零值，认为P在[i][j]位置包含M中同一列中高于这个零值或M中同一行中这个零值右侧的所有值的总和。
输入矩阵M的大小范围为[3x3 ... 900x900]。
如果两个矩阵的大小都不大于20，则以与输入矩阵M相同的格式打印矩阵P，不打印P的尺寸。
# 如果M的尺寸大于20x20，则只打印P的最右边最下面的子矩阵，尺寸为20x20。
在任何情况下，在（子）矩阵之后的下一行也要打印。所有被替换的零的总和。
'''
'''
Example 
Input
3
4 6
1 1 1 0 2 3
2 0 1 0 0 2
1 0 0 0 0 0
2 2 2 2 0 0
Output
1 1 1 5 2 3
2 4 1 2 4 2
1 1 2 0 2 5
2 2 2 2 2 5
32
'''
def task03( matrix ):
    total=0
    p = [['.' for j in range(C)] for i in range(R)]
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 0:
                a = 0
                b = 0
                for m in range(i):
                    a = a + matrix[m][j]
                for n in range(j+1,C):
                    b = b + matrix[i][n]
                p[i][j] = a + b
                total = total + a + b
            else:
                p[i][j] = matrix[i][j]
    if R <= 20:
        for item in p:
            print(*item)
        print(total)
    else:
        new=[]
        for i in range(R-20,R):
            new.append(p[i][C-20:])
        for item in new:
            print(*item)
        print(total)



'Task 04'
# Modify the input NxN matrix of integers in the following way.
# All matrix items which are located outside the main diagonal
# and outside the antidiagonal (secondary diagonal)  remain unchanged.
# The contents of the diagonals is rotated 90 degrees to the left
# (anti-clockwise) around the center of the matrix.
# The examples below illustrate the meaning of
#  "rotation of diagonals 90 degrees to the left."
# The size of input matrix M is in range[3x3 .. 300x300].
# Print the modified matrix in the same format as the input matrix,
# do not print its dimensions .
'''
Example 1
Input
4
7 7
1 0 0 0 0 0 4
0 1 0 0 0 4 0
0 0 1 0 4 0 0
0 0 0 5 0 0 0
0 0 2 0 3 0 0
0 2 0 0 0 3 0
2 0 0 0 0 0 3
Output
4 0 0 0 0 0 3
0 4 0 0 0 3 0
0 0 4 0 3 0 0
0 0 0 5 0 0 0
0 0 1 0 2 0 0
0 1 0 0 0 2 0
1 0 0 0 0 0 2

Example 2
Input
4
6 6
10 33 44 33 44 21  
33 11 33 44 20 44  
44 33 12 19 44 33  
33 44 18 13 33 44  
44 17 44 33 14 33  
16 44 33 44 33 15 
Output
21 33 44 33 44 15
33 20 33 44 14 44
44 33 19 13 44 33
33 44 12 18 33 44
44 11 44 33 17 33
10 44 33 44 33 16
'''
def task04( matrix ):
    ar2 = list(map(list, zip(*matrix)))
    ar2 = ar2[::-1]
    for i,j in zip(range(R),range(R)):
        matrix[i][j]=ar2[i][j]
        matrix[i][R-j-1]=ar2[i][R-j-1]
    for k in matrix:
        print(*k)



'Task 05'
# Modify the input NxN matrix of integers in the following way.
# All values which are at the border of the matrix
# are equal to the value at position [0][0] in the original matrix.
# All values which are at distance 1 from the border of the matrix
# are equal to the value at position [1][1] in the original matrix.
# All values which are at distance 2 from the border of the matrix
# are equal to the value at position [2][2] in the original matrix.
# And so on, up to the center of the matrix.
# In general:
# All values which are at distance k ( 0 <= k <= (N-1)//2 )
# from the border of the matrix are equal to the value
# at position [k][k] in the original matrix.
# The distance of a position [x][y] to the border is the
# minimum number of other positions between the border
# and the given position, in any of the four directions - up, down, left, right.
# The size of the matrix is not be modified.
# The size of input matrix is in range[2x2 .. 300x300].
# Print the modified matrix in the same format as the input matrix,
# do not print its dimensions .

'''
Example
Input
5
7 7
2 3 4 5 6 7 1
1 6 3 4 5 6 7
7 6 5 4 3 2 1
4 4 4 4 4 4 4
2 1 2 1 2 1 3
1 2 3 4 5 6 7
4 4 5 5 6 1 2
Output
2 2 2 2 2 2 2
2 6 6 6 6 6 2
2 6 5 5 5 6 2
2 6 5 4 5 6 2
2 6 5 5 5 6 2
2 6 6 6 6 6 2
2 2 2 2 2 2 2
'''
def task05( matrix ):
    p = [[matrix[0][0] for j in range(C)] for i in range(R)]
    for l in range(1,int(R/2)+1):
        flag = matrix[l][l]
        for i in range(l,R-l):
            for j in range(l,R-l):
                p[i][j] = flag

    for item in p:
        print(*item)


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#               I N P U T    R E A D I N G
taskNo = int( input() )
R, C = map(int, input().split())
arr2d = []
for i in range( R ):
    row = list(map(int, input().split()))
    arr2d.append( row )


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#             P R O C E S S I N G


if taskNo == 1:  task01( arr2d )
if taskNo == 2:  task02( arr2d )
if taskNo == 3:  task03( arr2d )
if taskNo == 4:  task04( arr2d )
if taskNo == 5:  task05( arr2d )
