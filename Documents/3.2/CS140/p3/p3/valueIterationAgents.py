# valueIterationAgents.py
# -----------------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
  """
      * Please read learningAgents.py before reading this.*

      A ValueIterationAgent takes a Markov decision process
      (see mdp.py) on initialization and runs value iteration
      for a given number of iterations using the supplied
      discount factor.
  """
  def __init__(self, mdp, discountRate = 0.9, iters = 100):
    """
      Your value iteration agent should take an mdp on
      construction, run the indicated number of iterations
      and then act according to the resulting policy.

      Some useful mdp methods you will use:
          mdp.getStates()
          mdp.getPossibleActions(state)
          mdp.getTransitionStatesAndProbs(state, action)
          mdp.getReward(state, action, nextState)
    """
    self.mdp = mdp
    self.discountRate = discountRate
    self.iters = iters
    self.values = util.Counter() # A Counter is a dict with default 0

    """Description:
    Assigns a value to every state in the game by computing the Q-value of every legal action at each state 
    and taking the max value of that to be the state's Q-value. (Essentially the V* equation from the slides)
    """
    """ YOUR CODE HERE """
    states = self.mdp.getStates() #returns all states in game
    #values = self.values.copy() #dictionary keys = state(coordinates), values = value at that state
    
    #print self.mdp.getPossibleActions(self.mdp.getStartState())
    #self.iters is the value at cmd line next to -i
    for _ in range(self.iters):
      values = self.values.copy() #declare here so that it updates values per iteration
      for state in states:
        possibleActions = self.mdp.getPossibleActions(state) #legal actions of state
        qValues = []
        for possibleAction in possibleActions:
          #print qValues
          qValues.append(self.getQValue(state, possibleAction))  
        if len(qValues) > 0: #avoid max() arg is an empty seq. error
          values[state] = max(qValues)
          #print values[state]      
      self.values = values #update new self.values
      
    #util.raiseNotDefined()
    """ END CODE """

  def getValue(self, state):
    """
      Return the value of the state (computed in __init__).
    """
    return self.values[state]

    """Description:
    [Enter a description of what you did here.]
    """
    """ YOUR CODE HERE """
    
    util.raiseNotDefined()
    """ END CODE """

  def getQValue(self, state, action):
    """
      The q-value of the state action pair
      (after the indicated number of value iteration
      passes).  Note that value iteration does not
      necessarily create this quantity and you may have
      to derive it on the fly.
    """
    """Description:
    Implementation of Q*(s,a) from the Bellman Equation
    """
    """ YOUR CODE HERE """
    #list of all successor states and its probabilities
    tnp = self.mdp.getTransitionStatesAndProbs(state, action) 
    #print tnp, action
    sumQ = 0
    for tState, prob in tnp:
      #print tState, prob
      sumQ += prob * (self.mdp.getReward(state, action, tState) + self.discountRate*self.getValue(tState))
    
    #print sumQ
    #print "==========="
    return sumQ
    util.raiseNotDefined()
    """ END CODE """

  def getPolicy(self, state):
    """
      The policy is the best action in the given state
      according to the values computed by value iteration.
      You may break ties any way you see fit.  Note that if
      there are no legal actions, which is the case at the
      terminal state, you should return None.
    """

    """Description:
    Takes in a state as an input and for every possible (legal) action,
    take the Q-value of each action and keep a record of the highest value.
    The highest Q-value is updated along with the corresponding action. 
    Return the action that causes the max Q-value.
    """
    """ YOUR CODE HERE """
    possibleActions = self.mdp.getPossibleActions(state) #actions of state
    
    maxQ = -1*float("inf")
    maxAction = None
    
    if len(possibleActions) == 0:
      return maxAction
    
    if len(possibleActions)> 0:
      for possibleAction in possibleActions:
        if self.getQValue(state, possibleAction) > maxQ:
          maxQ = self.getQValue(state, possibleAction)
          maxAction = possibleAction
          
    return maxAction
    util.raiseNotDefined()
    """ END CODE """

  def getAction(self, state):
    "Returns the policy at the state (no exploration)."
    return self.getPolicy(state)
