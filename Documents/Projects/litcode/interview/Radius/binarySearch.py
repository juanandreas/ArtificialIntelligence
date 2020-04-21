def binSearch(arr, left, right, t):
    mid = int((right+left)/2)

    if left <= right:
        if t == arr[mid]:
            return mid
        elif t < arr[mid]:
            return binSearch(arr, left, mid-1, t)
        elif t > arr[mid]:
            return binSearch(arr, mid+1, right, t)

    return -1



if __name__ == '__main__':
    arr1 = [1,2,3,4,6,7,9,10]
    t1 = 9
    print(binSearch(arr1, 0, len(arr1)-1, t1))

    arr2 = [2,3,4,10,40]
    t2 = 10
    print(binSearch(arr2, 0, len(arr2)-1, t2))