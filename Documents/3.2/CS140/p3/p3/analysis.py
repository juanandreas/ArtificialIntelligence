# analysis.py
# -----------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

######################
# ANALYSIS QUESTIONS #
######################

# Change these default values to obtain the specified policies through
# value iteration.

def question2():
  answerDiscount = 0.9
  answerNoise = 0.0
  """Description:
  removing noise will ensure that the agent will not miss and go to
  a hugely negative state. 
  """
  """ YOUR CODE HERE """

  """ END CODE """
  return answerDiscount, answerNoise

def question3a():
  answerDiscount = 0.3
  answerNoise = 0.0
  answerLivingReward = 0.0
  """Description:
  removing noise ecourages the agent to move east
  and lowering discount makes distant terminals to be worth less
  """
  """ YOUR CODE HERE """

  """ END CODE """
  return answerDiscount, answerNoise, answerLivingReward
  # If not possible, return 'NOT POSSIBLE'

def question3b():
  answerDiscount = 0.3
  answerNoise = 0.2
  answerLivingReward = 0.0
  """Description:
  original noise value encourages agent to start moving northwards
  lowering discount value makes the closer terminal worth more
  """
  """ YOUR CODE HERE """

  """ END CODE """
  return answerDiscount, answerNoise, answerLivingReward
  # If not possible, return 'NOT POSSIBLE'

def question3c():
  answerDiscount = 0.9
  answerNoise = 0.0
  answerLivingReward = 0.0
  """Description:
  a high discount rate makes distant terminal worth more
  getting rid of noise ensures that the agent does not go to a cliff state
  """
  """ YOUR CODE HERE """

  """ END CODE """
  return answerDiscount, answerNoise, answerLivingReward
  # If not possible, return 'NOT POSSIBLE'

def question3d():
  answerDiscount = 0.9999
  answerNoise = 0.1
  answerLivingReward = 0.0
  """Description:
  higher discount rate means distant terminal will be worth more
  and less noise will make the agent likely choose the path with higher rewards
  """
  """ YOUR CODE HERE """

  """ END CODE """
  return answerDiscount, answerNoise, answerLivingReward
  # If not possible, return 'NOT POSSIBLE'

def question3e():
  answerDiscount = 0.0
  answerNoise = 0.2
  answerLivingReward = 0.0
  """Description:
  discount of 0 makes terminal rewards worth nothing
  original noise value encourages agent to move northwards
  """
  """ YOUR CODE HERE """

  """ END CODE """
  
  return answerDiscount, answerNoise, answerLivingReward
  # If not possible, return 'NOT POSSIBLE'

def question6():
  answerEpsilon = None
  answerLearningRate = None
  """Description:
  a lower epsilon value encourages the agent to explore less states
  learningRate value is unclear, but it seems like the agent requires more
  iterations to be able to go deep enough into the other side of the bridge
  """
  """ YOUR CODE HERE """

  """ END CODE """
  #return answerEpsilon, answerLearningRate
  # If not possible, 
  return 'NOT POSSIBLE'

if __name__ == '__main__':
  print 'Answers to analysis questions:'
  import analysis
  for q in [q for q in dir(analysis) if q.startswith('question')]:
    response = getattr(analysis, q)()
    print '  Question %s:\t%s' % (q, str(response))
