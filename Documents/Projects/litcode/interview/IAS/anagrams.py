def isAnagram(a, b):
    freq = {}

    for c in a:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1
    
    for c in b:
        if c not in freq:
            return False
        
        freq[c] -= 1
        if freq[c] < 0:
            return False

    return True


if __name__ == '__main__':

    a = "ppp"
    b = "pppp"

    nani = isAnagram(a, b)
    print(nani)