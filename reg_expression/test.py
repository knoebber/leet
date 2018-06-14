from reg_expression import NonFiniteAutomata

def test_empty() :
  nfa = NonFiniteAutomata('')
  assert nfa.match('a') == False
  assert nfa.match('')  == True
  print 'pass empty'



def test_singleton() :
  nfa = NonFiniteAutomata('a')
  assert nfa.match('')  == False
  assert nfa.match('a') == True
  assert nfa.match('b') == False
  print 'pass singleton'

def test_simple_pattern() :
  nfa = NonFiniteAutomata('abcdef')
  assert nfa.match('')        == False
  assert nfa.match('a')       == False
  assert nfa.match('abc')     == False
  assert nfa.match('abcdeg')  == False
  assert nfa.match('abcdefg') == False
  assert nfa.match('abcdef')  == True
  print 'pass simple pattern'

def test_dot() :
  nfa = NonFiniteAutomata('a.c')
  assert nfa.match('')     == False
  assert nfa.match('a')    == False
  assert nfa.match('ab')   == False
  assert nfa.match('ac')   == False
  assert nfa.match('abc')  == True
  assert nfa.match('aic')  == True
  assert nfa.match('aicd') == False
  print 'pass dot'

def test_star() :
  nfa = NonFiniteAutomata('a*c')
  assert nfa.match('')     == False
  assert nfa.match('a')    == False
  assert nfa.match('ab')   == False
  assert nfa.match('acd')  == False
  assert nfa.match('aacd') == False
  assert nfa.match('cc')   == False
  assert nfa.match('acc')  == False
  assert nfa.match('ac')   == True
  assert nfa.match('c')    == True
  assert nfa.match('aaac') == True
  nfa = NonFiniteAutomata('a*')
  assert nfa.match('b') == False
  assert nfa.match('ab') == False
  assert nfa.match('aab') == False
  assert nfa.match('') == True
  assert nfa.match('a') == True
  assert nfa.match('aaa') == True
  print 'pass star'

def test_dot_star() :
  nfa = NonFiniteAutomata('.*c')
  assert nfa.match('')       == False
  assert nfa.match('a')      == False
  assert nfa.match('ab')     == False
  assert nfa.match('acd')    == False
  assert nfa.match('aacd')   == False
  assert nfa.match('acaacx') == False
  assert nfa.match('cc')     == True
  assert nfa.match('acc')    == True
  assert nfa.match('ac')     == True
  assert nfa.match('c')      == True
  assert nfa.match('abcaac') == True
  print 'pass dot star'


def test_suite() :
  test_empty()
  test_singleton()
  test_simple_pattern()
  test_dot()
  test_star()
  test_dot_star()



test_suite()
