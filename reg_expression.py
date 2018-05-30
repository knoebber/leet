class NonFiniteAutomata(object) :
  """
  creates a NFA that recognizes a pattern string
  """
  def __init__(self,pattern) :
    self.pattern = pattern
    self.start_state = State(pattern[0],True,len(pattern) == 1)
    if len(pattern) > 1 :
      curr = self.start_state
      for c in pattern[1:] :
        if c == '*' :
          curr.star = True
          continue
        state = State(c,False,False)
        state.prev_state = curr
        curr.next_state = state
        curr = state
      curr.is_end = True
      #curr.next_state = State(pattern[-1],False,True)
      #curr.next_state.prev_state = curr

  """
  determine if s matches the pattern string
  s      (str)  => the string to match
  return (bool) => whether the string matches
  """
  def match(self,s) :
    return self._match_r(s,0,self.start_state)

  def _match_r(self,s,i,state) :
    debug = False
    if debug : print i
    if debug : print s
    if i > len(s) - 1 :
      if debug : print 'i > len'
      return False
    c = s[i]
    if state.star :
      l = False
      if state.c == s[i] or state.c == '.' :
        l = self._match_r(s,i+1,state) #use same state again
      n  = self._match_r(s,i,state.next_state)
      return l or n
      #return  or self._match_r(s,i+1,state.next_state)
    else :
      if state.c != s[i] and state.c != '.' :
        if debug: print 'not equal'
        return False

    if debug : print state.next_state
    if not state.next_state :
      if debug :
        print 'not next state'
        print state.is_end
        print i
        print len(s) - 1
      return state.is_end and i == len(s) - 1
    else :
      return self._match_r(s,i+1,state.next_state)

  def print_states(self) :
    curr = self.start_state
    while True :
      print 'curr: '+curr.c
      print 'is start? ' + str(curr.is_start)
      print 'is end? ' + str(curr.is_end)
      print 'is star? ' + str(curr.star)
      if curr.prev_state :
        print 'prev state: ' +curr.prev_state.c
      else :
        print 'no prev'
      if curr.next_state :
        print 'next state: ' +curr.next_state.c
      else :
        print 'no next'
        break
      curr = curr.next_state


class State(object) :
  """
  creates one state for a NFA
  c     (char) => the character that can advance the state
  start (bool) => if its the starting state
  end   (bool) => if its the ending state
  """
  def __init__(self,c,start,end) :
    self.is_start = start
    self.is_end = end
    self.c = c
    self.next_state = None
    self.prev_state = None
    self.star = False




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
  print 'pass star'

def test_suite() :
  test_singleton()
  test_simple_pattern()
  test_dot()
  test_star()



test_suite()
nfa = NonFiniteAutomata('a*c')
"""
print nfa.match('c')
print nfa.match('ac')
print nfa.match('aac')
print nfa.match('aacc')
"""
