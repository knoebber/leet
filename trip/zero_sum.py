def tripplet(lst) :
  l = len(lst)
  if l < 3 :
    return []
  if l == 3 :
    return [(lst[0],lst[1],lst[2])]
  else :
    n = lst.pop()
    xs = tripplet(lst)
    new = []
    for t in xs :
      new += [(n,t[1],t[2])
             ,(t[0],n,t[2])
             ,(t[0],t[1],n)]
    return xs + new

def naive_zero_sum(lst) :
  return filter(lambda t : t[0] + t[1] + t[2] == 0,tripplet(lst))

