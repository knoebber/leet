def myAtoi(s) :
  if not s: return 0
  nums = ('0','1','2','3','4','5','6','7','8','9')
  s = s.strip()
  cutoff = len(s)
  for i in range(0,len(s)) :
    if s[i] not in nums and not (i==0 and (s[i] in ('-','+')))  :
      cutoff = i
      break
  s = s[:cutoff]
  try :
    x = int(s)
  except :
    return 0
  max_int = (2**31) -1
  min_int = -2**31
  if x > max_int : return max_int
  elif x < min_int : return min_int
  return x


print myAtoi('-5-') #should return -5
