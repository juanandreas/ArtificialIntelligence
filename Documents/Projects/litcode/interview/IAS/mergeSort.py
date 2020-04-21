def merge(arr, l, m, r):
    temp = [0] * (r-l+1)

    i = l
    j = m+1
    k = 0
    while i <= m and j <= r:

        curr_left = arr[i]
        curr_right = arr[j]

        if curr_left <= curr_right:
            temp[k] = curr_left
            i += 1
            k += 1
        if curr_right < curr_left:
            temp[k] = curr_right
            j += 1
            k += 1

    while i <= m:
        curr_left = arr[i]
        temp[k] = curr_left
        i += 1
        k += 1

    while j <= r:
        curr_right = arr[j]
        temp[k] = curr_right
        j += 1
        k += 1

    for i in range(l, r+1):
        arr[i] = temp[i - l]

def mergeSort(arr, l, r):

    if l < r:

        m = int((r+l)/2)

        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is")  
    print(arr) 
    mergeSort(arr, 0, len(arr)-1) 
    print("Sorted array is: ") 
    print(arr) 