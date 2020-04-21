def lazy_reverse(arr):
    print(arr[::-1])

def no_space_reverse(arr):
    
    end = len(arr)-1

    for i in range(len(arr)):
        if i == int(len(arr)/2):
            break
        right = arr[end-i]
        left = arr[i]
        arr[i] = right
        arr[end-i] = left

    print(arr)

def space_reverse(arr):

    new = []
    counter = len(arr)-1
    while(counter > -1):
        new.append(arr[counter])
        counter -= 1

    print(new)


if __name__=='__main__':

    A = [1,2,3]
    lazy_reverse(A)

    B = [1,2,3,4,5]
    no_space_reverse(B)

    C = [1,2,3,4,5,6,7]
    space_reverse(C)