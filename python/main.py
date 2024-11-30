def lengthOfLongestSubstring(s):
        save_char = {}
        max_sub = ''

        start = 0
        end = 0

        for index in range(len(s)):
            if (s[index] not in save_char) or (save_char[s[index]] < start):
                save_char[s[index]] = index

                end = index

                if len(max_sub) < (end - start + 1):
                    max_sub = s[start:(end + 1)]
            else:
                start = save_char[s[index]] + 1
                end = index

                save_char[s[index]] = index

                if len(max_sub) < (save_char[s[index]] - start + 1):
                    max_sub = s[start:(end + 1)]
        
        return max_sub

a = lengthOfLongestSubstring('pwwkew')
print(a)