symbols =
{
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
  if tens == 0 :
    if d == 4 :
      return f()+'IV'
    elif d == 9 :
      return f()+'IX'
    elif d < 5 :
      return f()+'I'*d
    elif d == 5 :
      return f()+'V'
    else :
      return f()+'V'+('I'*(d-5))
  elif tens == 1 :
    if d == 4 :
      return f()+'XL'
    elif d == 9 :
      return f()+'XC'
    elif d < 5 :
      return f()+'X'*d
    elif d == 5 :
      return f()+'L'
    else :
      return f()+'L'+('X'*(d-5))
  if debug: print 'after elif'

"""
converts a roman numeral string s to an integer
"""
def to_int(s) :
  return 0

