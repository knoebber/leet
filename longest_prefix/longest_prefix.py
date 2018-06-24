"""
find longest prefix
"""
def f_l_p(strings) :
  r = ''
  c = strings[0][0]
  i = 1 #word to check
  j = 0 #char to check
  while True :
    if i > len(strings) - 1 :
      i = 0
      j += 1
      r += c
      if j > len(strings[i]) - 1 :
        return r
      c = strings[i][j]
    if c != strings[i][j] :
      return r
    i = i + 1
