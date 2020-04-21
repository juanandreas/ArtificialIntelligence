def binary_search(arr, l, r, t):

    if l <= r:
        m = int((l+r)/2)

        if t == arr[m]:
            return m
        elif t < arr[m]:
            return binary_search(arr, l, m-1, t)
        elif t > arr[m]:
            return binary_search(arr, m+1, r, t)

    return -1

if __name__ == '__main__':

    arr = [0,1,2,3,4,5,6,7,8,9]
    t = 1
    print(binary_search(arr, 0, len(arr)-1, t))
