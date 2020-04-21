# Given a set of states, accept states, a string and a transition Table
# determine if the input string is accepted in this Nondeterministic Trellis Automata

# In this example, the string "AABD" results to the state D (top node)
# since state D is in {C, D}, the print out true, else false.

# Represent the transition table, and the given information in whatever u like
#            [D]
#            / \
#         [D]   [C]
#         / \   / \
#     [C,D]  [D]   [B]
#      / \   / \   / \
#   [A]   [A]   [B]   [D]
#   
#   Given:--------------------
#   States: {A, B, C, D}
#   Accept: {C, D}
#   String: AABD
# 
#
#   Transition Table:
#           A      B     C      D 
#        ___________________________
#       |      |      |      |      |
#   A   |  C,D |  B   |  D   |  C   |
#       |______|______|______|______|
#       |      |      |      |      |
#   B   |  A   |  B   |  C   |  D   |
#       |______|______|______|______|
#       |      |      |      |      |
#   C   |  D   |  B   |  C,D |  D   |
#       |______|______|______|______|
#       |      |      |      |      |
#   D   |  D   |  C   |  D   |  D   |
#       |______|______|______|______| 
#
#   Input:
#   ADA
#   BBBBBB
#   CDA
#
#   Output:
#   true
#   false
#   true