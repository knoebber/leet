"""
find longest prefix
"""
def f_l_p(strings) :
  r = ''
  if not strings or not strings[0] : return ''
  c = strings[0][0]
  i = 1 #word to check
  j = 0 #char to check
  l = len(strings)
  while True :
    if i > l - 1 :
      i = 0
      j += 1
      r += c
      if j > len(strings[i]) - 1 :
        return r
      c = strings[i][j]
    if j > len(strings[i]) - 1 :
      return r
    if c != strings[i][j] :
      return r
    i = i + 1
