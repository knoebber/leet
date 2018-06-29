def tripplet(lst) :
  l = len(lst)
  if l < 3 :
    return []
  if l == 3 :
    return [lst]
  else :
    n = lst.pop()
    xs = tripplet(lst)
    new = []
    for t in xs :
      new += [[n,t[1],t[2]]
             ,[t[0],n,t[2]]
             ,[t[0],t[1],n]]
    return xs + new

def naive_zero_sum(lst) :
  return map(list,set(
         map(lambda z: tuple(sorted(z)),
         filter(lambda t : t[0] + t[1] + t[2] == 0,tripplet(lst)))))



