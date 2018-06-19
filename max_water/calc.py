def calculate(points) :
  m = 0
  iterations = 0
  for i in xrange(0,len(points)) :
    debug = False
    for j in xrange(i+1,len(points)) :
      iterations +=1
      area = min(points[i],points[j]) * (abs((i+1) - (j+1)))
      if area > m :
        m = area
        if debug:
          print '-'*15
          print 'new max: ', m
          print i, ', ' ,j
          print '(',i+1,',',points[i],'),(',j+1,',',points[j],')'
          print '-'*15
  print iterations
  return m


"""
optimized version of calculate
"""
def f_calc(points) :
  points = zip(range(1,len(points)+1),points)
  return 0

            #x:  1,2,3,4,5  , (5-2) = 3 : 3*4 = 12
print calculate([2,4,3,6,10])

"""
sorted by x location (default)
(1,2)
(2,4)
(3,3)
(4,6)
(5,10)

sorted by height
(5,10)
(4,6)
(2,4)
(3,3)
(1,2)

naive: visit every pair
how can we improve?

some way to sort pairs of points by x location distance and height
the winner will be the first element of the sorted list

so make a list of pairs of points from points
zip points, range
sort points... how ??
is there some way to divide and conquer?
there will be a max height, where anything higher won't matter, and higher numbers can
be disregarded, or changed.
in above example , this would be 6. (maybe doesn't matter)

new strategy:
start from lowest height, check everything. increase height by one, only check those where it's
high enough. eventually we will be checking very few as less are as high

need to find ways to eliminate swathes of values by knowing something because of the
way its sorted
"""
