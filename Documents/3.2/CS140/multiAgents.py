# multiAgents.py
# --------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
  """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
  """


  def getAction(self, gameState):
    """
    You do not need to change this method, but you're welcome to.

    getAction chooses among the best options according to the evaluation function.

    Just like in the previous project, getAction takes a GameState and returns
    some Directions.X for some X in the set {North, South, West, East, Stop}
    """
    # Collect legal moves and successor states
    legalMoves = gameState.getLegalActions()
    #print legalMoves
    # Choose one of the best actions
    scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
    #print scores
    bestScore = max(scores)
    bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
    chosenIndex = random.choice(bestIndices) # Pick randomly among the best

    "Add more of your code here if you want to"

    return legalMoves[chosenIndex]

  def evaluationFunction(self, currentGameState, action):
    """
    Design a better evaluation function here.

    The evaluation function takes in the current and proposed successor
    GameStates (pacman.py) and returns a number, where higher numbers are better.

    The code below extracts some useful information from the state, like the
    remaining food (oldFood) and Pacman position after moving (newPos).
    newScaredTimes holds the number of moves that each ghost will remain
    scared because of Pacman having eaten a power pellet.

    Print out these variables to see what you're getting, then combine them
    to create a masterful evaluation function.
    """
    # Useful information you can extract from a GameState (pacman.py)
    successorGameState = currentGameState.generatePacmanSuccessor(action)
    newPosition = successorGameState.getPacmanPosition()
    oldFood = currentGameState.getFood()
    newGhostStates = successorGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

    "*** YOUR CODE HERE ***"
    nextFoodLocations = oldFood.asList()
    foodList = []
    
    #subroutine for finding the nearest food
    for food in nextFoodLocations:
      foodList.append(util.manhattanDistance(food, newPosition))
    fDist = min(foodList)
    
    newGhostPosition = newGhostStates[0].getPosition()

    gDist = util.manhattanDistance(newPosition, newGhostPosition)
    
    ######################IDEA#######################################
    #if ghost is scared, prioritize all evaluation on eating food!!!#
    #################################################################
    
    
    
    prioritize = (3*gDist)/(fDist+1)
    # if gDist/fDist > 1, ghost is farther away than nearby food, so food is ok
    # if gDist/fDist < 1, then food is farther away than ghost, so get away from ghost
    return prioritize + successorGameState.getScore()
    
def scoreEvaluationFunction(currentGameState):
  """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
  """
  return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
  """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
  """

  def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
    self.index = 0 # Pacman is always agent index 0
    self.evaluationFunction = util.lookup(evalFn, globals())
    self.treeDepth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
  """
    Your minimax agent (question 2)
  """

  def getAction(self, gameState):
    """
      Returns the minimax action from the current gameState using self.treeDepth
      and self.evaluationFunction.

      Here are some method calls that might be useful when implementing minimax.

      gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

      Directions.STOP:
        The stop direction, which is always legal

      gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

      gameState.getNumAgents():
        Returns the total number of agents in the game
    """
    "*** YOUR CODE HERE ***"

    return self.minimaxDecision(gameState)
    util.raiseNotDefined()
   
  #book pseudocode
  def minimaxDecision(self, state):
    #starts at depth 0
    v = -1*float("inf")
    bestMove = None
    
    #finds argMax of legalActions
    arg = []
    for action in state.getLegalActions(0):
      arg.append(scoreEvaluationFunction(state.generateSuccessor(0, action)))
    argMax = arg.index(max(arg))
    #print '=============================='
    #print 'this is legalActions:', state.getLegalActions(0)
    #print 'this is arg list:', arg
    #print 'this is index of argMax:', argMax
    #print 'this is value of argMax:', state.getLegalActions(0)[argMax]
    
    #print self.minValue(0, state.generateSuccessor(0, state.getLegalActions(0)[argMax]), 1)
    
    for action in state.getLegalActions(0):
      bestValue = v
      v = max(v, self.minValue(0, state.generateSuccessor(0, state.getLegalActions(0)[argMax]), 1))
      #compares previous utility value and extracts the action of max v
      if v > bestValue:
        bestMove = action
        
    #print 'this is best move:', bestMove
    return bestMove
    
  def maxValue(self, depth, state):
    if depth == self.treeDepth:
      return self.evaluationFunction 
    v = -1*float("inf")
    for action in state.getLegalActions(0):
      if action != Directions.STOP: #removes Directions.STOP
        v = max(v, self.minValue(depth, state.generateSuccessor(0, action), 1))
    return v
      
  def minValue(self, depth, state, ghostCount):
    if depth == self.treeDepth:
      return self.evaluationFunction
    v = float("inf")
    for action in state.getLegalActions(ghostCount):
      if action != Directions.STOP: #removes Directions.STOP
        if ghostCount == state.getNumAgents()-1:
          v = min(v, self.maxValue(depth+1, state.generateSuccessor(ghostCount, action)))
        else:
          #if not all ghosts have made a move
          #treat all min levels between previous max and the next max as the same depth
          v = min(v, self.minValue(depth, state.generateSuccessor(ghostCount, action), ghostCount+1))
    return v
   
class AlphaBetaAgent(MultiAgentSearchAgent):
  """
    Your minimax agent with alpha-beta pruning (question 3)
  """

  def getAction(self, gameState):
    """
      Returns the minimax action using self.treeDepth and self.evaluationFunction
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
  """
    Your expectimax agent (question 4)
  """

  def getAction(self, gameState):
    """
      Returns the expectimax action using self.treeDepth and self.evaluationFunction

      All ghosts should be modeled as choosing uniformly at random from their
      legal moves.
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
  """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
  """
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

class ContestAgent(MultiAgentSearchAgent):
  """
    Your agent for the mini-contest
  """

  def getAction(self, gameState):
    """
      Returns an action.  You can use any method you want and search to any depth you want.
      Just remember that the mini-contest is timed, so you have to trade off speed and computation.

      Ghosts don't behave randomly anymore, but they aren't perfect either -- they'll usually
      just make a beeline straight towards Pacman (or away from him if they're scared!)
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

