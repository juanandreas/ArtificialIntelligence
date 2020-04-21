import sys
import collections

if __name__ == '__main__':

    f = open(sys.argv[1], "r")
    for i in f:
        print(i, end="")

    asshole = ["Fuck", "fuck", "ass", "ass"]
    count = collections.Counter(asshole)
    print(count)
    f.close()