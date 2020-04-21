from collections import defaultdict
def find_longest_unique_substring(s):

    d = defaultdict(int)
    l = 0
    r = 0
    counter = 0
    max_window = 0

    while(r < len(s)):
        r_char = s[r]
        d[r_char] += 1
        if d[r_char] > 1:
            counter += 1

        r += 1

        while(counter > 0):
            l_char = s[l]
            d[l_char] -= 1

            if d[l_char] == 1:
                counter -= 1

            l += 1

        max_window = max(max_window, (r-l))

    return max_window

if __name__ == '__main__':

    s = "abcccccccccccccdefgss"

    longest_substr = find_longest_unique_substring(s)
    
    print(longest_substr)