'''
m = 3 employees
n = 5 workdays
       0    1    2    3    4                - index
ad = [yyy, yyy, ynn, yyn, yyn]
       1    2    3    4    5                - days 1,2,3,4,5

                  0       1       2         - employee 0,1,2
3rd DAY: ad[2] =  y       n       n
4th DAY: ad[3] =  y       y       n
5th DAY: ad[4] =  y       y       n

employees 1 and 2 are absent on the third day
and employee 2 is out on the 4th and 5th day

maxStreak function must return an integer denoting the 
maximum number of consecutive days where all the employees 
of the project are present
'''

def maxStreak(m, data):
    max_streak = 0
    streak = 'Y'*m
    
    temp = 0
    for attendance in data:

        if attendance == streak:
            temp += 1
            max_streak = max(max_streak, temp)
        else:
            temp = 0

    
    return max_streak


if __name__ == '__main__':

    m = 3
    data = ['YYY', 'YYY', 'YNN', 'YYN', 'YYN']
    print(maxStreak(m, data))

    m = 2
    data = ['YN', 'NN']
    print(maxStreak(m, data))

    m = 4
    data = ['YYYY', 'YYYY', 'YYYY', 'YYYY']
    print(maxStreak(m, data))
