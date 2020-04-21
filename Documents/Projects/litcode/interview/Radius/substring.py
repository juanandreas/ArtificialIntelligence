from collections import defaultdict
import sys
def find_longest_unique_substring(s):

    max_window = 0
    left = 0
    right = 0
    counter = 0

    slen = len(s)

    freq = {}
    for char in s:
        if char not in freq:
            freq[char] = 0
    # {
    #     a:0,
    #     b:0,
    #     c:0,
    #     d:0,
    #     f:0
    # }

    while right < slen:
        # letter at right end of window
        curr_end_char = s[right]
        freq[curr_end_char] += 1

        # if one type of character was seen, 
        # count of characters decreases by one
        if freq[curr_end_char] > 1:
            counter += 1

        right += 1
        # shrink left side of window until duplicate 
        # is removed from window view
        while counter > 0:
            curr_begin_char = s[left]
            freq[curr_begin_char] -= 1

            # once duplicate is removed, get outta there
            if freq[curr_begin_char] == 1:
                counter -= 1

            left += 1


        # update size of max window if needed
        max_window = max((right-left), max_window)

    return max_window


if __name__ == '__main__':

    s = "abccabcddf"

    longest_substr = find_longest_unique_substring(s)
    
    print(longest_substr)