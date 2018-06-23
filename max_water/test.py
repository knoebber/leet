from calc import calculate,f_calc
from random import randint
from time import time

def test_versions() :
  iterations = 10
  length = 1000
  max_size   = 50
  for i in range(0,iterations) :
    l = []
    for j in range(0,length) :
      l.append(randint(1,max_size))
    start = time()
    naive = calculate(l)
    end = time()
    elapsed = end - start
    print 'naive took: ', elapsed
    start = time()
    optimized = f_calc(l)
    end = time()
    elapsed = end - start
    print 'optimized took: ', elapsed
    try :
      assert naive == optimized
    except :
      print 'failed on: ',l
      raise Exception ('Failed test versions')
  print 'passes!'

test_versions()
