def solve(threshold, size, H):
    start = H[0]
    steps = 1

    i = 0
    while(i < size):
        if (H[i+1] - start) >= threshold:
            steps += 1
            break
        elif (H[i+2] - start) >= threshold:
            steps += 1
            break
        else:
            i += 2
            steps+=1

    return steps

if __name__ == '__main__':
    
    ###########TEST 1################################################
    threshold1 = 2
    Happy1 = [1,2,3]
    size1 = len(Happy1)
    minNum = solve(threshold1, size1, Happy1)

    answer = 2
    if minNum == answer:
        print("Cool, {}".format(minNum))
    else:
        print("Expected {}, but got {}".format(answer, minNum))
    #################################################################

    ###########TEST 2################################################
    threshold2 = 4
    Happy2 = [1,2,3,4,5]
    size2 = len(Happy2)
    minNum = solve(threshold2, size2, Happy2)

    answer = 3
    if minNum == answer:
        print("Cool, {}".format(minNum))
    else:
        print("Expected {}, but got {}".format(answer, minNum))
    #################################################################

    ###########TEST 3################################################
    threshold3 = 99
    Happy3 = [1,2,3,4,5,100]
    size3 = len(Happy3)
    minNum = solve(threshold3, size3, Happy3)

    answer = 4
    if minNum == answer:
        print("Cool, {}".format(minNum))
    else:
        print("Expected {}, but got {}".format(answer, minNum))
    #################################################################
