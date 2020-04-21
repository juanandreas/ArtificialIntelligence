import time, winsound

def countdown(t):
    loop = t
    while True:
        while t > -1:
            mins, secs = divmod(t, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat, end='\r')
            time.sleep(1)
            t -= 1

        t = loop
        import winsound
        frequency = 300  # Set Frequency To 2500 Hertz
        duration = 200  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)

if __name__ == '__main__':
    countdown(18)