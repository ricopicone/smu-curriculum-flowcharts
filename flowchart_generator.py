import sys
import graphviz as gv
import functools
from pprint import pprint

#### functions and classes ####

def apply_styles(graph, styles):
  graph.graph_attr.update(
    ('graph' in styles and styles['graph']) or {}
  )
  graph.node_attr.update(
    ('nodes' in styles and styles['nodes']) or {}
  )
  graph.edge_attr.update(
    ('edges' in styles and styles['edges']) or {}
  )
  return graph

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

  def __init__(self, name, term):
    self.name = name
    self.term = term
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

def new_course(name,term):
  global courses
  try: courses
  except NameError: courses = {}
  courses.update({name: course(name,term)})

#### build the graph ####

graph = functools.partial(gv.Graph, format='svg')
digraph = functools.partial(gv.Digraph, format='svg')

execfile(sys.argv[1])

nodes_by_term = [[],[],[],[],[],[],[],[]] # initialize
terms_by_name = ['1a','1b','2a','2b','3a','3b','4a','4b']
for course_key in courses.keys():
  course_term_index = terms_by_name.index(courses[course_key].term)
  nodes_by_term[course_term_index].append(courses[course_key].name)

edges = [] # initialize
edges_cluster = [] # initialize
for course_key in courses.keys():
  for prereq in courses[course_key].prereqs:
    edges.append(
      ((prereq,courses[course_key].name),{'style': 'solid'})
    )
  for coprereq in courses[course_key].coprereqs:
    edges.append(
      ((coprereq,courses[course_key].name),{'style': 'dashed'})
    )

g = digraph()
g.attr(newrank='true',compound='true')
for i,term in enumerate(terms_by_name):
  name_now = 'cluster_'+str(i)
  h = add_nodes(digraph(name_now), nodes_by_term[i])
  h.graph_attr.update(rank='same',color='black')
  g.subgraph(h)
  if i > 0:
    edges_cluster.append(
      (
        (nodes_by_term[i-1][0],nodes_by_term[i][0]),
        {'ltail': 'cluster_'+str(i-1),'lhead': name_now,'style': 'invis'}
      )
    )

g = add_edges(g, edges_cluster)
g = add_edges(g, edges)

styles = {
  'graph': {
    # 'label': 'Prerequisite structure',
    'fontsize': '16',
    'fontcolor': 'black',
    'fontname': 'Courier',
    'bgcolor': 'white',
    'rankdir': 'TB',
  },
  'nodes': {
    'fontname': 'Courier',
    'shape': 'rectangle',
    'fontcolor': 'white',
    'color': 'white',
    'style': 'filled',
    'fillcolor': '#006699',
  },
  'edges': {
    'style': 'dashed',
    'color': 'black',
    'arrowhead': 'open',
    'fontname': 'Courier',
    'fontsize': '12',
    'fontcolor': 'black',
  }
}


g = apply_styles(g, styles)
g.render('img/g')

