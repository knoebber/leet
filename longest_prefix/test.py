from longest_prefix import f_l_p

def test_flp() :
  assert f_l_p(['a']) == 'a'
  assert f_l_p(['a','a']) == 'a'
  assert f_l_p(['aa','a']) == 'a'
  assert f_l_p(['aa','aax']) == 'aa'
  assert f_l_p(['aabazb','aax']) == 'aa'
  assert f_l_p(['aabazb','aabasl']) == 'aaba'
  assert f_l_p(['dog','racecar','car']) == ''
  assert f_l_p(['flower','flow','flight']) == 'fl'
  print 'passes!'


test_flp()
