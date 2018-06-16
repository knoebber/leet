from roman_converter import to_roman,to_int



def to_roman_basic() :
  assert to_roman(1)    == 'I'
  assert to_roman(5)    == 'V'
  assert to_roman(10)   == 'X'
  assert to_roman(50)   == 'L'
  assert to_roman(100)  == 'C'
  assert to_roman(500)  == 'D'
  assert to_roman(1000) == 'M'

def test_to_roman() :
  to_roman_basic()
  print 'all tests pass!'

test_to_roman()
