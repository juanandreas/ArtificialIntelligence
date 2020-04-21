# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
    i = low-1        # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index  
def quickSort(arr,low,high): 
    if low < high: 
  
        pi = partition(arr,low,high) 

        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 


def merge(arr, start, mid, end):
    sort = []
    i = start
    j = mid+1

    while i <= mid and j <= end:
        if arr[i] < arr[j]:
            sort.append(arr[i])
            i += 1
        elif arr[i] > arr[j]:
            sort.append(arr[j])
            j += 1
        elif arr[i] == arr[j]:
            sort.append(arr[i])
            sort.append(arr[j])
            i += 1
            j += 1

    # residual in left side
    while i <= mid:
        sort.append(arr[i])
        i += 1

    # residual in right side
    while j <= end:
        sort.append(arr[j])
        j += 1

    print(arr)
    for i in range(start, end+1):
        arr[i] = sort[i - start]
        i += 1

    print("-------------------------------")

    print("left", end=" ")
    print(arr[start:mid+1])
    print("right", end=" ")
    print(arr[mid+1:end+1])
    print("sort", sort)

    print("\nstart: ", start)
    print("end: ", end)
    print(arr)

    print("===============================")

def mergeSort(arr, start, end):
    if start < end:
        mid = int((start + end)/2)

        print("mergeSort(arr, start, mid): ", arr[start:mid+1])
        mergeSort(arr, start, mid)

        print("mergeSort(arr, mid+1, end): ", arr[mid+1:end+1])
        mergeSort(arr, mid+1, end)

        merge(arr, start, mid, end)

if __name__ == '__main__':
    # arr = [2,0,6,3,4,1,9,8,7,5]
    
    # quickSort(arr, 0, 9)
    # print(arr)

    arr = [2,0,6,3,4,1,9,8,7,5]
    mergeSort(arr, 0, len(arr)-1)
    print(arr)