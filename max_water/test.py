from calc import calculate,f_calc
from random import randint

def test_versions() :
  iterations = 100
  max_length = 20
  max_size   = 50
  for i in range(0,iterations) :
    l = []
    for j in range(0,max_length) :
      l.append(randint(1,max_size))
    try :
      assert calculate(l) == f_calc(l)
    except :
      print 'failed on: ',l
      raise Exception ('Failed test versions')
  print 'passes!'

test_versions()
