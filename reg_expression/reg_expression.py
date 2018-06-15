class NonFiniteAutomata(object) :
  """
  creates a NFA that recognizes a pattern string
  """
  def __init__(self,pattern,debug=False) :
    if debug :
      print 'constructing ',pattern
    self.pattern = pattern
    self.debug = debug
    if len(pattern) > 0 :
      self.start_state = State(pattern[0],True,len(pattern) == 1)
    else :
      self.start_state = None
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
      if debug :
        self.print_states()
      #curr.next_state = State(pattern[-1],False,True)
      #curr.next_state.prev_state = curr

  """
  determine if s matches the pattern string
  s      (str)  => the string to match
  return (bool) => whether the string matches
  """
  def match(self,s) :
    if self.start_state and self.start_state.star and self.start_state.is_end and not s :
      return True
    if not self.pattern :
      return not s
    return self._match_r(s,0,self.start_state)

  def _match_r(self,s,i,state) :
    if self.debug : print i
    if self.debug : print s
    if i > len(s) - 1 :
      if self.debug : print 'i > len'
      return False
    c = s[i]
    if state.star :
      if state.is_end and i == len(s) - 1 and c == state.c:
        return True
      l = False
      if state.c == s[i] or state.c == '.' :
        l = self._match_r(s,i+1,state) #use same state again
      n = False
      if state.next_state :
        n  = self._match_r(s,i,state.next_state)
      return l or n
      #return  or self._match_r(s,i+1,state.next_state)
    else :
      if state.c != s[i] and state.c != '.' :
        if self.debug: print 'not equal'
        return False

    if self.debug : print state.next_state
    if not state.next_state :
      if self.debug :
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





