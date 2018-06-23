"""
naive solution
"""
def calculate(points) :
  m = 0
  for i in xrange(0,len(points)) :
    for j in xrange(i+1,len(points)) :
      area = min(points[i],points[j]) * (abs((i+1) - (j+1)))
      if area > m :
        m = area
  return m

0
"""
optimized version of calculate
first step should be too make a single pass over points and remove all
that have taller points surrounding them
"""
def f_calc(heights) :
  m = 0
  t = 0
  for i in xrange(0,len(heights)) :
    if heights[i] > t :
      t = heights[i]
    else:
      continue
    for j in xrange(0,len(heights)) :
      area = min(heights[i],heights[j]) * (abs((i+1) - (j+1)))
      if area > m :
        m = area
  return m

print f_calc([5,1,5])
