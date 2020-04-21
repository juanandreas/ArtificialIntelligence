"""
Calculate a running average:

Given stream of integers (say a continuous flow of updates received by a service) 
write a function to calculate a running average. 
Numbers in the input stream could be very large numbers (order of 2^31)

public class RunningAverage {
      public static double getRunningAvg(int latest) {
      }
}
"""

count = 0
s = 0

def getRunningAvg(new_number):
  count += 1
  s += new_number
  latest_running_avrg = (latest_running_avrg + new_number) / count
  
  return latest_running_avrg
  

"""
ads_1.txt, ads_2.txt
date . campaign id . badAds . goodAds
01/01/12,  111,        100 .    200
01/03/15,  222,        100 .    200
01/01/12,  111,        100 .    200


conditions:
ignore campaign ids < 0
ignore campaigns that served < 100 ads on a particular day

Q: Calculate total ads served for each campaign by date, considering above conditions.
py spark,

"""

"""
-- Assume you have a table name ADS_FEB with these columns
-- |ADS_DATE   |HOUR      | CAMPAIGN_ID           | ADS                    |
-- |2017-02-01 | 01       | 122                   | 20                     |
-- |2017-02-01 | 02       | 122                   | 90                     |
-- |2017-02-02 | 01       | 122                   | 10                     |
-- |2017-02-07 | 01       | 126                   | 10                     |
-- |2017-02-07 | 02       | 126                   | 10                     |
-- |2017-02-07 | 03       | 126                   | 10                     |
-- |2017-02-08 | 04       | 126                   | 20                     |
-- |2017-02-08 | 05       | 126                   | 20                     |
-- |2017-02-08 | 06       | 126                   | 20                     |
-- |2017-02-08 | 07       | 126                   | 60                     |


1. provide number of ads for each day for each campaign id? 
result should have ads_date, campaign id, total number ads

2. provide number of ads for each day for each campaign id, 
but exclude all campaigns that had less than 100 ads per day?
"""

select ADS_DATE, CAMPAIGN_ID, SUM(ADS) 
from ADS_FEB
GROUP BY ADS_DATE, CAMPAIGN_ID
having SUM(ADS) >= 100



"""
Implement a linked list.
The implementation, among other things, 
should include a method *split()* that would find the center of the list
and return the two halves of it
"""

class Node:
  
  def __init__(self, val):
    self.val = val
    self.next = None
    self.length = 0
    
  def append(self, new_Node):
    self.next = new_Node
    self.length += 1
  
  def split(self):
    ptr = self
    
    # discovers length
    # list_len = 0
    # while ptr != None:
    #   list_len += 1
    #   ptr = ptr.next
    list_len = self.length
      
    ptr = self
    i = 0
    first = Node(0)
    while i < list_len/2:
      first.next = ptr
      ptr = ptr.next
      i += 1
      
    second = Node(0)
    while i < list_len:
      second.next = ptr
      ptr = ptr.next
      i += 1
      
    return first.next, second.next
    
"""
Write a function that accepts a list of 0’s and 1’s 
and returns the length of the longest sequence of 1’s.

int foo(int[] input){
}

For example
1011011101    -- returns 3
101110001111  -- returns 4
1011010101    -- returns 2
"""

def longest_substring(s):
  
  max_window = 0
  shrink = False
  l = 0
  r = 0
  
  
  while r < len(s):
    
    curr_r = s[r]
    
    r += 1
    
    if curr_r == '0':
      shrink = True
    
    while shrink:
      curr_l = s[l]
      l += 1
      
      if l == r:
        shrink = False
        
    max_window = max(max_window, r-l)
    
  
  return max_window
    
  
  
  
