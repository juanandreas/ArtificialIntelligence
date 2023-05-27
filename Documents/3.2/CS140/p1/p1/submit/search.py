# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def startingState(self):
    """
    Returns the start state for the search problem 
    """
    util.raiseNotDefined()

  def isGoal(self, state): #isGoal -> isGoal
    """
    state: Search state

    Returns True if and only if the state is a valid goal state
    """
    util.raiseNotDefined()

  def successorStates(self, state): #successorStates -> successorsOf
    """
    state: Search state
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
    """
    util.raiseNotDefined()

  def actionsCost(self, actions): #actionsCost -> actionsCost
    """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
    """
    util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.startingState()
  print "Is the start a goal?", problem.isGoal(problem.startingState())
  print "Start's successors:", problem.successorStates(problem.startingState())
  """
  
  startState = problem.startingState()
  dirStack = util.Stack() #stack status
  visited = [] #keeps track of already visited nodes
  plan = [] #direction plan for pacman
  
  if problem.isGoal(startState):
    return plan
  else:
    Visit(problem, startState, dirStack, visited, plan)

  return plan
  
  util.raiseNotDefined()

def Visit(problem, stateCalledOn, dirStack, visited, plan):
  visited.append(stateCalledOn)
  dirStack.push(stateCalledOn)
  
  successors = problem.successorStates(stateCalledOn)
  
  if len(plan) == 0: #if a plan is empty, keep exploring
    for successor in successors[::-1]:
      newState = successor[0]
      if newState not in visited: 
        Visit(problem, newState, dirStack, visited, plan)
        if problem.isGoal(dirStack.pop()):
          #call stackToPlan() to convert correct path stack into plan
          dataToPlan(dirStack, plan, newState)
      
def dataToPlan(data, plan, goal):
  from game import Directions
  n = Directions.NORTH
  s = Directions.SOUTH
  w = Directions.WEST
  e = Directions.EAST
  
  #stack goal for first direction reference
  data.push(goal)
  
  for x in range(len(data.list)-1):
    if data.list[x][1] - data.list[x+1][1] == 1:
       plan.append(s)
    if data.list[x][1] - data.list[x+1][1] == -1:
       plan.append(n)
    if data.list[x][0] - data.list[x+1][0] == 1:
       plan.append(w)
    if data.list[x][0] - data.list[x+1][0] == -1:
       plan.append(e)
  
  #pop off goal to prevent unneeded executions of stackToPlan()
  data.pop()
       
  return plan
      

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"
  startState = (problem.startingState(), None)
  dirQueue = util.Queue() #queue status
  visited = [] #keeps track of already visited nodes
  P = {} # parent dictionary: P = {child:parent}
  
  if problem.isGoal(startState[0]):
    return []
  else:
    visited.append(startState[0])
    dirQueue.push(startState)
    
    while not dirQueue.isEmpty():
      currentState = dirQueue.pop()
      
      #stop exploring when goal is found
      if problem.isGoal(currentState[0]):
        return backTrack(startState, currentState, P)
      
      successors = problem.successorStates(currentState[0])
      
      for successor in successors:
        if successor[0] not in visited:
          newNode = successor[0],successor[1]
          #P = {child:parent}
          P.update({newNode:currentState})
          visited.append(successor[0])
          dirQueue.push(newNode)
          
  util.raiseNotDefined()

def backTrack(start, goal, P):
  path = [goal] #(1,1)
  plan = []
  while path[-1][0] != start[0]:
    plan.append(path[-1][1])
    path.append(P[path[-1][0],path[-1][1]])  
  plan.reverse()
  return plan
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  #node = [((x,y), dir), cost]
  node = (problem.startingState(), None)
  nodeCost = 0
  frontier = util.PriorityQueue()
  frontier.push(node, nodeCost)
  explored = []
  P = {} #parent dictionary for identifying path {child:parent}
  while not frontier.isEmpty():
    #preserves priority, which is node's cost before popped
    nodeCost = frontier.heap[0][0]
    node = frontier.pop()
 
    if problem.isGoal(node[0]):
      goal = node
      start = (problem.startingState(),None)
      return backTrack(start, goal, P)
      
    explored.append(node[0])
    successors = problem.successorStates(node[0])
    for successor in successors:
      childNode = successor[0]
      childAction = successor[1]
      pathCost = successor[2] #of parent to child
      child = (childNode, childAction)
      if childNode not in explored:
        #c(m) = c(n) and c(n,m)
        #the cost of child node m = 
        #cost of previous node n + cost of getting from node n to m
        P.update({child:node})
        childCost = nodeCost+pathCost
        frontier.push(child, childCost)

  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  #queue format = [((x,y), dir), f(n)=g(n)+h(n)]
  gTotal = 0
  h = heuristic(problem.startingState(), problem)
  node = (problem.startingState(), None)
  frontier = util.PriorityQueue() 
  frontier.push(node, gTotal+h)
  explored = [] 
  P = {} #parent dictionary for identifying path {child:parent}
  while not frontier.isEmpty():
    #preserves priority, which is node's cost before popped
    nodeCost = frontier.heap[0][0]
    node = frontier.pop()
    gTotal = nodeCost - heuristic(node[0], problem) #cost of start -> current
    if problem.isGoal(node[0]):
      goal = node
      start = (problem.startingState(),None)
      return backTrack(start, goal, P)
      
    explored.append(node[0])
    successors = problem.successorStates(node[0])
    for successor in successors:
      childNode = successor[0]
      childAction = successor[1]
      g = successor[2] #cost of path from parent to child
      h = heuristic(successor[0], problem)
      child = (childNode, childAction)
      if childNode not in explored:
        P.update({child:node})
        frontier.push(child, h+g+gTotal)
  util.raiseNotDefined()
    

  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
