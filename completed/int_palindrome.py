from math import log10,ceil

"""
checks if an integers digits are a palindrome
without converting to str
"""
def is_palindrome(x) :
  if x < 0  : return False
  elif x < 10 : return True
  y = x
  reverse = 0
  n = ceil(log10(x)) #the amount of digits the number has
  m = 10**(n-1)
  while y > 0 :
    d = y % 10
    reverse += (d*m)
    y /= 10
    m /= 10
  return reverse == x


def is_palindrome_simple(x) :
  return str(x) == str(x)[::-1]


print is_palindrome(-4331)
print is_palindrome(0)
print is_palindrome(10)
print is_palindrome(55)
print is_palindrome(516)
print is_palindrome(515)
print 'simple test'
print is_palindrome_simple(-4331)
print is_palindrome_simple(0)
print is_palindrome_simple(10)
print is_palindrome_simple(55)
print is_palindrome_simple(516)
print is_palindrome_simple(515)


