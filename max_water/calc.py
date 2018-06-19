def calculate(points) :
  m = 0
  for i in xrange(0,len(points)) :
    debug = False
    for j in xrange(i+1,len(points)) :
      area = min(points[i],points[j]) * (abs((i+1) - (j+1)))
      if area > m :
        m = area
        if debug:
          print '-'*15
          print 'new max: ', m
          print i, ', ' ,j
          print '(',i+1,',',points[i],'),(',j+1,',',points[j],')'
          print '-'*15
  return m


            #x:  1,2,3,4,5  , (5-2) = 3 : 3*4 = 12
print calculate([2,4,3,6,10])

