def binarySearch(A, l, r, t):

    if l <= r:
        
        m = (r-l) / 2

        if A[m] == t:
            return m
        elif A[m] > t:
                return binarySearch(A, l, m-1, t)
        elif A[m] < t:
                return binarySearch(A, m+1, r, t)
    
    return -1


if __name__ == '__main__':

    A = [0,1,2,3,4,5,6,7,8,9]

    A = [12, 543, 9594, 900000]

    t = 12

    binarySearch(A, 0, len(A)-1, t)