"""
leetcode zigzag conversion

s = PAYPALISHIRING  len = 14

--------------------
numRows = 3

0 1 2 3 4 5 6
P   A   H   N
A P L S I I G
Y   I   R

out = PAHNAPLSIIGYIR
--------------------
numRows = 4

0 1 2 3 4 5 6
P     I     N
A   L S   I G
Y A   H R
P     I

out = PINALSIGYAHRPI
--------------------
numRows = 5

0 1 2 3 4 5
P       H
A     S I
Y   I   R
P L     I G
A       N

out = PHASIYIRPLIGAN
"""

def convert(s, numRows) :
  if numRows <= 1 : return s
  numCols = len(s)#TODO calculate how many cols are needed
  grid = [['']*numCols for i in range(0,numRows)]
  print_grid(grid)
  result  = [''] * numRows
  row = 0
  col = 0
  for c in s :
    grid[row][col] = c
    result[row] += c

    if row == numRows - 1 :
      down = False
    elif row == 0 :
      down = True

    if down : row += 1
    else :
      row -= 1
      col += 1
  return ''.join(result)



def print_grid(g) :
  for row in g :
    print row

print convert('PAYPALISHIRING',3)
#print convert('ABC',1)
