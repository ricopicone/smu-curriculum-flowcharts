#### functions and classes ####

def add_nodes(graph, nodes):
  for n in nodes:
    if isinstance(n, tuple):
      graph.node(n[0], **n[1])
    else:
      graph.node(n)
      return graph

def add_edges(graph, edges):
  for e in edges:
    if isinstance(e[0], tuple):
      graph.edge(*e[0], **e[1])
    else:
      graph.edge(*e)
      return graph

class course:
  """Defines a course"""

  def __init__(self, name):
    self.name = name
    self.prereqs = []
    self.coreqs = []
    self.coprereqs = []
    self.styles = {}

  def add_prereq(self, prereq):
    self.prereqs.append(prereq)

  def add_coreq(self, coreq):
    self.coreqs.append(coreq)

  def add_coprereq(self, coprereq):
    self.coprereqs.append(coprereq)

  def add_style(self, style_key, style_value):
    self.styles.update({style_key: style_value})