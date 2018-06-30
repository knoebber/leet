"""
find all tripplets in a list
"""
def tripplet(lst) :
  l = len(lst)
  if l < 3 :
    return []
  if l == 3 :
    return [lst]
  else :
    x = lst.pop()
    xs = tripplet(lst)
    new = []
    for t in xs :
      new += [[x,t[1],t[2]]
             ,[t[0],x,t[2]]
             ,[t[0],t[1],x]]
    return xs + new
"""
finds all tripplets in lst
filters these to ones that add to 0
then removes duplicates tripplets by sorting
and making into a set
VERY slow
"""
def naive_zero_sum(lst) :
  return map(list,set(
         map(lambda z: tuple(sorted(z)),
         filter(lambda t : t[0] + t[1] + t[2] == 0,tripplet(lst)))))

"""
finds tripplets
by moving through sorted list
"""
def fast_tz(lst) :
  l = len(lst)
  if l < 3 : return []
  lst = sorted(lst)
  if lst[0]  >  0 : return []
  if lst[-1] <  0 : return []
  result = set()
  small = 0
  big = l - 1
  while lst[small] <= 0 and lst[big] >= 0 :
    if abs(lst[small]) > lst[big] :
      i = big
      while i < l and lst[i] <= 0 :
        j = i - 1
        while i >= 0 and lst[j] >= 0 :
          if lst[small] + lst[i] + lst[j] == 0 :
            result.add((lst[small],lst[j],lst[i]))
          j -= 1
        i -=1
      small += 1
    else :
      i = small
      while i < l and lst[i] <= 0 :
        j = i + 1
        while j < l and lst[j] <= 0 :
          if lst[big] + lst[i] + lst[j] == 0 :
            result.add((lst[i],lst[j],lst[big]))
          j +=1
        i +=1
      big -= 1
  return map(lambda x : list(x), result)
