#PGE Practices 02

# practices 02

# Common input format
# -------------------
# (Read the tasks descriptions below before reading this paragraph.)
# All tasks in practices 02 set share common data input format:
# The first line contains the number of the task (1 - 5).
# The second line contains the dimensions R and C of the input rectangular matrix.
# The first is the vertical size R (number of rows),
# the second is the horizontal size C (number of columns),
# they are separated by space.
# Next, there are R lines of input, each contains C values separated by spaces.
# Each line contains values of the corresponding matrix row.
# The input always contain exactly one data set of one task.
# In the evaluation system, the code is run repeatedly, each time with different input.

# Solution code structure
# -----------------------
# The code reads the input data, including the number of the task.
# Next, it runs a function or a block of code which accepts the input data
# and computes and prints the solution to it.
# It is recommended to wrap the solution of each task in a separate function,
# an example (not obligatory!) structure of the code
# is illustrated by the contents of this file.


# ================================================================================
# Task 01
# For the given matrix,  print in ascending order,
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
    # your solution here
    pass

# ================================================================================
# Task 02

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
    # your solution here
    pass


# ================================================================================
# Task 03

# For a given rectangular matrix M, create a new matrix P,
# which dimensions are the same as the dimensions of M.
# For each non-zero value in M at position [i][j] it holds,
# that P contains the same value at position [i][j].
# For each zero value in M at position [i][j] it holds,
# that P contains at position [i][j] the sum of all values
# which are either above this zero in the same column in M
# or to the right of this zero in the same row in M.
# The size of input matrix M is in range[3x3 .. 300x300].
# If both matrix sizes are not bigger than 20, print matrix P
# in the same format as the input matrix M, do not print the
# dimensions of P.
# If the size of M is bigger than 20 x 20, print only the
# rightmost bottommost submatrix of P of size 20x20.
# In any case, print also, after the (sub)matrix, on the next line,
# the total of all values by which were the zeros substituted.


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
    # your solution here
    pass


# ================================================================================
# Task 04

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
    # your solution here
    pass


# ================================================================================
# Task 05

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
    # your solution here
    pass


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

'''
Public data
The public data set is intended for easier debugging and approximate program correctness checking. The public data set is stored also in the upload system and each time a student submits a solution it is run on the public dataset and the program output to stdout and stderr is available to him/her.
Link to the public data set
'''
