def comparelist(L1, L2):
    # if L1 == L2:
    #     return True
    # else:
    #     return False

    # base case
    if len(L1) != len(L2):
        return False
    
    for i in range(len(L1)):
        if L1[i] != L2[i]:
            return False

    return True

def compareMat(M1, M2):
    # if M1 == M2:
    #     return True
    # else:
    #     return False

    # base case
    if len(M1) != len(M2):
        return False

    for i in range(len(M1)):
        if comparelist(M1[i], M2[i]) == False:
            return False

    return True

if __name__=='__main__':

    L1 = ["ass", "dick", "butt"]
    # L1_twin = ["ass", "dick", "butt"]

    L2 = ["ass", "butt", "dick"]

    print(comparelist(L1, L2))

    M1 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    M1_twin = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [1,2,2]
    ]

    M2 = [
        [7,8,9],
        [4,5,6],
        [1,2,3]
    ]
     
    print(compareMat(M1, M1_twin))

