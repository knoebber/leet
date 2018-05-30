class NonFiniteAutomata(object) :
  """
  creates a NFA that recognizes a pattern string
  """
  def __init__(self,pattern) :
    self.pattern = pattern
    self.start_state = State(pattern[0],True,False)
    curr = self.start_state
    for c in pattern[1:-1] :
      state = State(c,False,False)
      curr.next_state.append(state)
      curr = state
    curr.next_state.append(State(pattern[-1],False,True))

  """
  determine if s matches the pattern string
  s      (str)  => the string to match
  return (bool) => whether the string matches
  """
  def match(self,s) :
    if not self.pattern : return False
    state = self.start_state
    for c in s :
      if c != state.c : return False
      if not state.next_state : break

      state = state.next_state[0]
    return state.is_end

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
    self.next_state = []




def test_singleton() :
  nfa = NonFiniteAutomata('a')
  assert nfa.match('')  == False
  assert nfa.match('a') == True
  assert nfa.match('b') == False
  print 'passes'

def test_simple_pattern() :
  nfa = NonFiniteAutomata('abcdef')
  #assert nfa.match('')        == False
  #assert nfa.match('a')       == False
  #assert nfa.match('abc')     == False
  #assert nfa.match('abcdeg')  == False
  #assert nfa.match('abcdefg') == False
  assert nfa.match('abcdef')  == True
  print 'passes'


def test_suite() :
  test_singleton()
  test_simple_pattern()



test_suite()
