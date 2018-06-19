from roman_converter import to_roman,to_int

"""
test values < 100
"""
def to_roman_small() :
  assert to_roman(1)  == 'I'
  assert to_roman(2)  == 'II'
  assert to_roman(3)  == 'III'
  assert to_roman(4)  == 'IV'
  assert to_roman(9)  == 'IX'
  assert to_roman(11) == 'XI'
  assert to_roman(14) == 'XIV'
  assert to_roman(19) == 'XIX'
  assert to_roman(21) == 'XXI'
  assert to_roman(40) == 'XL'
  assert to_roman(44) == 'XLIV'
  assert to_roman(43) == 'XLIII'
  assert to_roman(51) == 'LI'
  assert to_roman(59) == 'LIX'
  assert to_roman(78) == 'LXXVIII'
  assert to_roman(90) == 'XC'
  assert to_roman(94) == 'XCIV'
  assert to_roman(96) == 'XCVI'
  assert to_roman(99) == 'XCIX'
  print 'pass small test'

"""
test basic cases
"""
def to_roman_basic() :
  assert to_roman(1)    == 'I'
  assert to_roman(5)    == 'V'
  assert to_roman(10)   == 'X'
  assert to_roman(50)   == 'L'
  assert to_roman(100)  == 'C'
  assert to_roman(500)  == 'D'
  assert to_roman(1000) == 'M'
  print 'pass basic to roman tests'

def test_to_int() :
  for i in range(0,4000) :
    roman = to_roman(i)
    convt = to_int(roman)
    assert convt == i

def test_roman_conversion() :
  to_roman_small()
  to_roman_basic()
  test_to_int()
  print 'all tests pass!'

test_roman_conversion()
