# 1) Take an integer input from the user and store it in `rowSize`.
# (This represents the total height of the diamond pattern.)
# 2) Decide how many rows the top half of the diamond should have:
# a) If `rowSize` is even, set `halfDiamRow = rowSize/2`
# b) If `rowSize` is odd, set `halfDiamRow = rowSize/2 + 1`
# (This ensures the middle row is included in the upper half.)
# 3) Initialize `space = halfDiamRow - 1`.
# (This controls leading spaces before printing numbers in the upper half.)
# 4) Print the upper half of the diamond:
# a) Use an outer loop `i` from 1 to `halfDiamRow` (inclusive) for rows.
# b) For each row:
# i) Print `space` number of blank spaces using an inner loop.
# ii) Decrease `space` by 1 after printing spaces.
# iii) Set `num = 1` to start printing numbers from 1 in that row.
# iv) Print `(2*i - 1)` numbers in the row using another inner loop:
# - Print the current `num` without moving to the next line.
# - Increase `num` by 1 after each print.
# v) Print a newline to move to the next row.
rowSize= int(input("Enter the row size:"))
if rowSize%2==0:
    halfDiamRow= rowSize/2
else:
    halfDiamRow= (rowSize//2)+1
space= halfDiamRow-1    
