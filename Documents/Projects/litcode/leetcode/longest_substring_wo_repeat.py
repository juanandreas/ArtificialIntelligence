from collections import defaultdict

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    begin = 0
    end = 0
    counter = 0
    
    max_window = 0

    table = defaultdict(int)
    
    slen = len(s)
    while end < slen:
        table[s[end]] += 1
        if table[s[end]] > 1:
            counter += 1
        
        end += 1
            
        while counter > 0:
            table[s[begin]] -= 1
            if table[s[begin]] == 1:
                counter -= 1
            begin += 1
        
        max_window = max((end-begin), max_window)
                
    return max_window


if __name__ == '__main__':
        
    print(lengthOfLongestSubstring("abcabcbb"))

    print(lengthOfLongestSubstring("a"))

    print(lengthOfLongestSubstring("au"))

    print(lengthOfLongestSubstring("dvdf"))