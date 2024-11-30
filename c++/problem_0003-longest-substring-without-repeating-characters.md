# <span style="color: #f43f5e" >3. Longest Substring Without Repeating Characters</span>

## <span style="color: #10b981">Description:</span>
**Link:** https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Given a string s, find the length of the longest substring without repeating characters.

 

**Example 1:**
```cpp
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```
**Example 2:**
```cpp
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```
**Example 3:**
```cpp
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

**Constraints:**
```cpp
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
```


## <span style="color: #10b981">Solution:</span>

### <span style="color: #ea580c">* Approach 1: Sliding window</span>
#### Pseudo code:
```cpp
s = "" => return 0

i = 0, j = 0, maxLen = INT_MIN
unordered_map<char, int> mp

while j < s.size():
    value of s[j] add 1

    while value of s[j] > 1:
        value of s[i] reduce 1
        i++

    j++;
    maxLen = max(maxLen, j - i)
return maxLen

```
#### Code:
```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s == "") return 0;    // Trường hợp chuỗi rỗng return 0

        int i = 0, j = 0;
        int maxLen = INT_MIN;
        unordered_map<char, int> mp;   // Map chứa tần số của char

        while (j < s.size()) {
            mp[s[j]]++;   // Mỗi lần di chuyển thì cộng tần số của giá trị đó vào
            
            // Xét nếu tần số nó lớn hơn 1 thì phải di chuyển i cho tới khi gặp được giá trị s[i] đó mà đã có trước đó.
            // Để biết khi nào gặp được thì cứ -1, nếu giá trị giảm xuống 1 thì nghĩa là i đã đến đúng chỗ. (đồng thời đã xóa hết tần số của mấy số trước đó để bắt đầu xét lại từ vị trí i)
            while (mp[s[j]] > 1) {
                mp[s[i]]--;
                i++;
            }

            j++;   // Tăng j lên để di chuyển tiếp
            maxLen = max(maxLen, j - i);    // Max giữa giá trị cũ và khoảng cách từ j tới i
        }

        return maxLen;
    }
};
```

### <span style="color: #ea580c">* Approach 2: Kiểm tra trùng lặp bằng map và find</span>
#### Pseudo code:
```cpp
unordered_map<char, int> mp
start = 0
maxLen = 0

for (i := 0) -> s.size():
    if ((not find s[i] in mp) and (mp[s[i]] >= start)):
        start = mp[s[i]] + 1
    mp[s[i]] = i
    maxLen = max(maxLen, distance between i and start)

return maxLen

```
#### Code:
```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> mp;
        int start = 0, maxLen = 0;

        for (int i = 0; i < s.size(); i++) {
            // Tìm nếu có s[i] trong map thì index của nó phải lớn hơn vị trí bắt đầu chuỗi substr đang xét
            if (mp.find(s[i]) != mp.end() && mp[s[i]] >= start) {
                start = mp[s[i]] + 1;   // Bắt đầu từ vị trí của char bị lặp + 1
            }

            mp[s[i]] = i;   // Thay index vào giá trị của key char trong map để lưu giữ index có giá trị đó gần nhất với substr đang xét
            maxLen = max(maxLen, i - start + 1);
        }

        return maxLen;
    }
};
```

### <span style="color: #ea580c">* Approach 3: ...</span>
#### Pseudo code:
```cpp

```
#### Code:
```cpp

```