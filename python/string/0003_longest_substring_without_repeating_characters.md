# <span style="color: #f43f5e" >3. Longest Substring Without Repeating Characters</span>

## <span style="color: #10b981">Description:</span>
**Link:** https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Given a string s, find the length of the longest substring without repeating characters.

**Example 1:**
```py
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```
**Example 2:**
```py
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```
**Example 3:**
```py
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
```

Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

**Constraints:**
```py
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
```

## <span style="color: #10b981">Solution:</span>

### <span style="color: #ea580c">* Approach 1: Normal, use dict</span>
#### Pseudo code:
```py
Idea: 
- Chạy hết toàn bộ string
    + Nếu [ không nằm trong dict ] hoặc [ nằm trong dict nhưng value thấp hơn start - điểm đang xét ] :
        => Lưu index của giá trị đó (create hoặc replace old)
        => Xét so với string max cũ khi đã thay đổi đến index mới

    + Nếu [ ngược lại ] :
        => Vì có giá trị bị lặp, nên ta di chuyển đến vị trí [ char bị lặp + 1 ] cho str tiếp theo
```
#### Code:
```py
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s: return 0

        save_char = {}
        max_sub = ''

        # Start và end của str đang xét
        start = 0
        end = 0

        for index in range(len(s)):
            end = index

            if (s[index] not in save_char) or (save_char[s[index]] < start):
                save_char[s[index]] = index

                if len(max_sub) < (end - start + 1):
                    max_sub = s[start:(end + 1)]

            else:
                start = save_char[s[index]] + 1

                save_char[s[index]] = index

        return len(max_sub)
```

### <span style="color: #ea580c">* Approach 2: ...</span>
#### Pseudo code:
```py

```
#### Code:
```cpp

```

### <span style="color: #ea580c">* Approach 3: ...</span>
#### Pseudo code:
```py

```
#### Code:
```py

```