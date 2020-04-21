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
latest_running_avrg = 0
def getRunningAvg(new_number):
    global count
    global s
    global latest_running_avrg
    count += 1
    latest_running_avrg = (((count-1)*latest_running_avrg)/count) + (new_number/count)
    s += new_number
    return latest_running_avrg


if __name__ == '__main__':

        getRunningAvg(2)
        getRunningAvg(100)
        getRunningAvg(52)
        getRunningAvg(43)
        getRunningAvg(90)
        x = getRunningAvg(10)
        print(x)