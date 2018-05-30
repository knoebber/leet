"""
reverse an integer
123 => 321
result should be between -2^31, 2^31 -1
"""

def reverse(x) :
  r = int(str(x)[::-1]) if x >= 0 else int(str(x)[:0:-1]) *-1
  return 0 if r > (2**31) - 1 or r < -2**31 else r


print reverse(-512)
