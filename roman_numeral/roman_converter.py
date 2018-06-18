symbols = {
  0 : ['I','V'],
  1 : ['X','L'],
  2 : ['C','D'],
  3 : ['M']
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

def _to_roman(tens,i,) :
  if i == 0: return ''

  f = lambda: _to_roman(tens+1,i/10)
  d = i%10

  if   d == 0 : return f()
  if   d == 4 : return f() + symbols[tens][0] + symbols[tens][1]
  elif d == 9 : return f() + symbols[tens][0] + symbols[tens+1][0]
  elif d <  5 : return f() + symbols[tens][0] * d
  elif d == 5 : return f() + symbols[tens][1]
  else        : return f() + symbols[tens][1] + (symbols[tens][0]*(d-5))

values = {
  'I'  : 1,
  'IV' : 4,
  'V'  : 5,
  'IX' : 9,
  'X'  : 10,
  'XL' : 40,
  'L'  : 50,
  'XC' : 90,
  'C'  : 100,
  'CD' : 400,
  'D'  : 500,
  'CM' : 900,
  'M'  : 1000
}
"""
converts a roman numeral string s to an integer
"""
def to_int(s) :
  i = 0
  while len(s) > 0 :
    if s[:2] in values :
      i += values[s[:2]]
      s = s[2:]
    else :
      i += values[s[0]]
      s = s[1:]
  return i
