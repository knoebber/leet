symbols = {
  0:['I','V'],
  1:['X','L'],
  2:['C','D'],
  3:['M']
}

"""
converts an integer i into a roman numeral
precondition: i < 4000

114 => CXIV
119 => CIX
149 => CXLIX
"""
def to_roman(i) :
  return _to_roman(0,i)

def _to_roman(tens,i,debug=False) :
  if debug:
    print 'tens: ',tens
    print 'i: ',i
  if i == 0:
    if debug:
      print 'i == 0'
    return ''
  f = lambda: _to_roman(tens+1,i/10)
  d = i%10
  if debug:
    print 'digit: ',d
    print 'new i: ',i

  if d == 0 :
    if debug:
      print 'd == 0' 
    return f()
  if d == 4 :
    return f() + symbols[tens][0] + symbols[tens][1]
  elif d == 9 :
    return f() + symbols[tens][0] + symbols[tens+1][0]
  elif d < 5 :
    return f() + symbols[tens][0]*d
  elif d == 5 :
    return f() + symbols[tens][1]
  else :
    return f() + symbols[tens][1] + (symbols[tens][0]*(d-5))

"""
converts a roman numeral string s to an integer
"""
def to_int(s) :
  return 0
