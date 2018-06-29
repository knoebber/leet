from zero_sum import *

def basic_test(f) :
  assert f([]) == []
  assert f([1]) == []
  assert f([1,2]) == []
  assert f([1,2,3]) == []
  assert f([-1,0,1]) == [[-1,0,1]]
  assert f([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2],[-1, 0, 1]]
  print 'passes basic'

def suite() :
  basic_test(lambda lst : naive_zero_sum(lst))


suite()

