def longest_palindrome_naive(s):
  start = 0
  longest = ''
  curr = ''
  for i in range(0,len(s)):
    for j in range(start,len(s)):
      curr += s[j]
      print(curr)
      if curr[::-1] == curr and len(curr)> len(longest) :
        longest = curr
    curr = ''
    start+=1
  print "----------"
  print longest
  print "----------"
  return longest



def longest_palindrome(s) :
  if not s :
    return ''
  s2 = findB(s)
  p = [0] * len(s2)

  c = 0
  r = 0

  m = 0
  n = 0

  for i in range(1,len(s2)) :
    if i>r :
      p[i] = 0
      m = i -1
      n = i+1
    else :
      i2 = c*2 - i
      if p[i2]<(r-i-1) : 
        p[i] = p[i2]
        m = -1
      else :
        p[i] = r - i
        n = r + 1
        m = i*2 - n
    while m>= 0 and n<len(s2) and s2[m] == s2[n] :
      p[i]+=1
      m -= 1
      n+=1
    if (i+p[i])>r :
      c = i
      r = i+p[i]
  length = 0
  c = 0

  for i in range(1,len(s2)) :
    if length < p[i] :
      length = p[i]
      c = i
  ss = s2[c-length:c+length+1]
  return ''.join(removeB(ss))


"""
find boundries in string s
"""
def findB(cs) :
  if not cs : return "||"

  cs2 = [0] * ((len(cs)*2) + 1)
  for i in xrange (0,len(cs2)-1,2) :
    cs2[i] = '|' #add a | boundry at every other spot
    cs2[i+1] = cs[i/2] #fill the boundries in 
  cs2[len(cs2)-1] = '|'
  return cs2

def removeB(cs) :
  if not cs :
    return ""
  cs2 = [0]*((len(cs)-1)/2)
  for i in range(0,len(cs2)) :
    cs2[i] = cs[i*2+1]
  cs2[i] = cs[i*2+1]
  return cs2

print longest_palindrome("aaabazbaaabbbzzaaakiudfs")
