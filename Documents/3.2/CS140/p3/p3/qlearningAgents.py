# qlearningAgents.py
# ------------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import random,util,math

class QLearningAgent(ReinforcementAgent):
  """
    Q-Learning Agent

    Functions you should fill in:
      - getQValue
      - getAction
      - getValue
      - getPolicy
      - update

    Instance variables you have access to
      - self.epsilon (exploration prob)
      - self.alpha (learning rate)
      - self.discountRate (discount rate)

    Functions you should use
      - self.getLegalActions(state)
        which returns legal actions
        for a state
  """
  def __init__(self, **args):
    "You can initialize Q-values here..."
    ReinforcementAgent.__init__(self, **args)

    self.values = util.Counter() # key: (state, action) -- value: default 0


  def getQValue(self, state, action):
    """
      Returns Q(state,action)
      Should return 0.0 if we never seen
      a state or (state,action) tuple
    """
    """Description:
    just returns the value at the state,action tuple
    """
    """ YOUR CODE HERE """
    return self.values[(state,action)]
    util.raiseNotDefined()
    """ END CODE """

  def getValue(self, state):
    """
      Returns max_action Q(state,action)
      where the max is over legal actions.  Note that if
      there are no legal actions, which is the case at the
      terminal state, you should return a value of 0.0.
    """
    """Description:
    assign the value of a state with the maximum of computed values for every action
    of a state.
    """
    """ YOUR CODE HERE """
    legalActions = self.getLegalActions(state)
    qValues = []
    
    if len(legalActions) == 0:
      return 0.0
      
    if len(legalActions) > 0:
      for legalAction in legalActions:
        qValues.append(self.getQValue(state, legalAction))

    return max(qValues)
    util.raiseNotDefined()
    """ END CODE """

  def getPolicy(self, state):
    """
      Compute the best action to take in a state.  Note that if there
      are no legal actions, which is the case at the terminal state,
      you should return None.
    """
    """Description:
    like in q1, return the action that is associated with the max value
    however, since it is possible to have 2 actions that produce equal values,
    do a pseudo-random picking of those values.
    """
    """ YOUR CODE HERE """
    legalActions = self.getLegalActions(state)
    maxQval = -1*float("inf")
    maxAction = []
    
    if len(legalActions) == 0:
      return None
    
    if len(legalActions) > 0:
      for legalAction in legalActions:
        temp = self.getQValue(state, legalAction)
        if temp > maxQval:
          maxQval = temp
          maxAction = [legalAction]
          
        #if an action has the same qValue of another action
        if temp == maxQval:
          maxAction.append(legalAction)
          
    maxAct = random.choice(maxAction)
    
    return maxAct
    
    util.raiseNotDefined()
    """ END CODE """

  def getAction(self, state):
    """
      Compute the action to take in the current state.  With
      probability self.epsilon, we should take a random action and
      take the best policy action otherwise.  Note that if there are
      no legal actions, which is the case at the terminal state, you
      should choose None as the action.

      HINT: You might want to use util.flipCoin(prob)
      HINT: To pick randomly from a list, use random.choice(list)
    """
    # Pick Action
    legalActions = self.getLegalActions(state)
    action = None

    """Description:
    a pseudo-random action is picked epsilon of the time or the optimal action is picked
    this is so that the agent doesn't greedily choose the optimal choice everytime
    because it does not always guarantee overall optimality in later iterations
    """
    """ YOUR CODE HERE """
    
    if len(legalActions) == 0:
      return action
    
    #flip a coin
    chance = util.flipCoin(self.epsilon)
    
    #decide whether to pick random action or policy
    if len(legalActions)> 0:
      if chance:
        #return self.getPolicy(state) 
        return random.choice(legalActions) #choose random epsilon of the time
      else:
        #return random.choice(legalActions)
        return self.getPolicy(state)
    
    util.raiseNotDefined()
    """ END CODE """

    #return action

  def update(self, state, action, nextState, reward):
    """
      The parent class calls this to observe a
      state = action => nextState and reward transition.
      You should do your Q-Value update here

      NOTE: You should never call this function,
      it will be called on your behalf
    """
    """Description:
    Piazza suggestion
    """
    """ YOUR CODE HERE """
    #value update equation from slide 27 M4
    discountValue = self.discountRate  
    self.values[(state,action)] += self.alpha * (reward + (discountValue * self.getValue(nextState)) - self.getQValue(state, action) )
    #util.raiseNotDefined()
    """ END CODE """

class PacmanQAgent(QLearningAgent):
  "Exactly the same as QLearningAgent, but with different default parameters"

  def __init__(self, epsilon=0.05,gamma=0.8,alpha=0.2, numTraining=0, **args):
    """
    These default parameters can be changed from the pacman.py command line.
    For example, to change the exploration rate, try:
        python pacman.py -p PacmanQLearningAgent -a epsilon=0.1

    alpha    - learning rate
    epsilon  - exploration rate
    gamma    - discount factor
    numTraining - number of training episodes, i.e. no learning after these many episodes
    """
    args['epsilon'] = epsilon
    args['gamma'] = gamma
    args['alpha'] = alpha
    args['numTraining'] = numTraining
    self.index = 0  # This is always Pacman
    QLearningAgent.__init__(self, **args)

  def getAction(self, state):
    """
    Simply calls the getAction method of QLearningAgent and then
    informs parent of action for Pacman.  Do not change or remove this
    method.
    """
    action = QLearningAgent.getAction(self,state)
    self.doAction(state,action)
    return action


class ApproximateQAgent(PacmanQAgent):
  """
     ApproximateQLearningAgent

     You should only have to overwrite getQValue
     and update.  All other QLearningAgent functions
     should work as is.
  """
  def __init__(self, extractor='IdentityExtractor', **args):
    self.featExtractor = util.lookup(extractor, globals())()
    PacmanQAgent.__init__(self, **args)

    # You might want to initialize weights here.
    self.weights = util.Counter() #default 0
    

  def getQValue(self, state, action):
    """
      Should return Q(state,action) = w * featureVector
      where * is the dotProduct operator
    """
    """Description:
    Implements the approximate q-function from q9.
    """
    """ YOUR CODE HERE """
    featureVectors = self.featExtractor.getFeatures(state, action)
    
    sum = 0
    for featureVector in featureVectors:
      sum += featureVectors[featureVector] * self.weights[featureVector]
    
    return sum
    
    util.raiseNotDefined()
    """ END CODE """

  def update(self, state, action, nextState, reward):
    """
       Should update your weights based on transition
    """
    """Description:
    'ApproximateQAgent uses the IdentityExtractor, 
    which assigns a single feature to every (state,action) pair.'
    
    This important line in the instructions is for updating all weight
    values with the formula provided in q9. For which I don't really understand
    the logic for doing so too well.......
    
    The updating for values is done by calculating the correction value
    to use for multiplication in the w_i from the formula provided.
    """
    """ YOUR CODE HERE """
    self.gamma = self.discountRate
    self.featureVectors = self.featExtractor.getFeatures(state, action)
    
    correction = reward + (self.gamma * self.getValue(nextState)) - self.getQValue(state,action) 
    
    #assign every state,action pair with the new feature value
    for featureVector in self.featureVectors:
     self.weights[featureVector] += self.alpha * correction * self.featureVectors[featureVector]
    
    #util.raiseNotDefined()
    """ END CODE """

  def final(self, state):
    "Called at the end of each game."
    # call the super-class final method
    PacmanQAgent.final(self, state)

    # did we finish training?
    if self.episodesSoFar == self.numTraining:
      # you might want to print your weights here for debugging
      util.raiseNotDefined()
