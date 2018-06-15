class NonFiniteAutomata(object) :
  def __init__(self,pattern,debug=False) :
    if debug:
      print 'pattern: ',pattern
    self.nodes = []
    self.debug = debug
    n = 0
    for i in range(0,len(pattern)) :
      c = pattern[i]
      if c == '*' :
        self.nodes[i-n-1].star = True
        n += 1
      else :
        self.nodes.append(Node(c))
    self.nodes.append(Node(None))
    #self.l = len(self.nodes)
    if debug :
      for n in self.nodes : n.print_info()

  def match(self,s) :
    if self.nodes[0].c is None : return not s
    return self._match(s,self.nodes)

  def _match(self,s,nodes) :
    node = nodes[0]
    if node.c is None :
      return not s

    if len(s) == 0 :
      if node.star and nodes[1].c is None :
        return True
      else:
        return False

    c = s[0]
    if node.star :
      if node.wild or node.c is c :
        return self._match(s[1:],nodes) or self._match(s,nodes[1:])
      else :
        return self._match(s,nodes[1:])
    if not node.wild and node.c is not c :
      return False
    return self._match(s[1:],nodes[1:])


class Node(object) :
  def __init__(self,c) :
    self.c = c
    self.star = False
    self.wild = c == '.'

  def print_info(self) :
    print '-'*15
    print 'symbol:', self.c
    print 'wild?: ', str(self.wild)
    print 'star?: ', str(self.star)
    print '-'*15

