# <span style="color: #f43f5e" >20. Valid Parentheses</span>

## <span style="color: #10b981">Description:</span>
**Link:** https://leetcode.com/problems/valid-parentheses/description/

Given a string s containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

**Example 1:**
```cpp
Input: s = "()"
Output: true
```
**Example 2:**
```cpp
Input: s = "()[]{}"
Output: true
```
**Example 3:**
```cpp
Input: s = "(]"
Output: false
```

**Constraints:**
```cpp
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
```

## <span style="color: #10b981">Solution:</span>

### <span style="color: #ea580c">* Approach 1: User regular expression</span>
#### Pseudo code:
```cpp

string symbolsContain
rexexp = "{}|[]|()";
map<char, bool> mp (những kí tự cần thiết thì true)
for (i := 0) -> s.len():
    if (mp[s[i]] = true) => symbolsContain += s[i]

if (symbolsContain.len() chẵn):
    do {
        symbolsContain = symbolsContain sau khi thay đổi những string khớp thành ""
        if (search(symbolsContain) không có):
            break
    } while true

    if (symbolsContain.empty() = true) => return true
    else: return false
else:
    return false
    
```
#### Code:
```cpp
class Solution {
public:
    bool isValid(string s) {
        string symbolsContain;
        regex regexp("\\{\\}|\\[\\]|\\(\\)");   // Tạo một pattern khớp {} or () or []

        unordered_map<char, bool> mp;    // map với key = kí tự và value = bool.
        mp['{'] = mp['('] = mp['['] = mp['}'] = mp[')'] = mp[']'] = true;

        // Lọc string ra những kí tự yêu cầu
        for (int i = 0; i < s.length(); i++) {
            if (mp[s[i]]) {
                symbolsContain += s[i];
            }
        }
        
        if (symbolsContain.length() % 2 == 0) {
            do {
                symbolsContain = regex_replace(symbolsContain, regexp, "");  // Thay thế hết những (), [], {} xếp ngay cạnh nhau bằng chuỗi rỗng để tiếp tục xét
                if (!regex_search(symbolsContain, regexp)) {
                    // Xét cho tới khi không tìm được một cặp nào như vậy nữa
                    break;
                }
            } while (true);

            // Nếu sau khi replace hết các cặp, nếu hết cặp thì nghĩa là ổn, còn không thì sẽ bị sai
            if (symbolsContain.empty()) {
                return true;
            } else {
                return false;
            }
        } else {
            // Nếu lẻ thì chắc chắn bị dư 1 kí tự nào đó không có đóng hoặc mở
            return false;
        }
    }
};
```

### <span style="color: #ea580c">* Approach 2: ...</span>
#### Pseudo code:
```cpp

```
#### Code:
```cpp

```

### <span style="color: #ea580c">* Approach 3: ...</span>
#### Pseudo code:
```cpp

```
#### Code:
```cpp

```