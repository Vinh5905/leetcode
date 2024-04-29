# <span style="color: #f43f5e" >14. Longest common prefix</span>

## <span style="color: #10b981">Description:</span>
**Link:** https://leetcode.com/problems/longest-common-prefix/description/

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

 

**Example 1:**
```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```
**Example 2:**
```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

**Constraints:**
```
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
```
## <span style="color: #10b981">Solution:</span>

### <span style="color: #ea580c">* Approach 1: Mỗi lần xét tìm đoạn substr chung</span>
#### Pseudo code:
```cpp
res = strs[0]
len = res.len()
for (i := 1) -> strs.size():
    while len > strs[i].len() or res != strs[i].substr(0, len):
        len--
        if len = 0 => return "" // empty string 
        res = res.substr(0, len)

return res
```
#### Code:
```cpp
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string res = strs[0];   // Biến lưu trữ result
        int len = res.size();   // Biến lưu trữ size của result

        for (int i = 1; i < strs.size(); i++) {   // Chạy hết các string trong vector
            // len > strs[i].size() : Kiểm tra len của đoạn result, nếu lớn hơn thì phải giảm xuống để bằng đoạn string
            // Nếu len nhỏ hơn hoặc bằng thì tiếp tục xét (trường hợp nhỏ hơn thì vẫn tiếp tục được vì điều kiện phía sau sẽ kiểm tra xem có bằng nhau không, nếu nhỏ hơn thì sẽ không bao giờ bằng => tiếp tục giảm len)
            // res != strs[i].substr(0, len) : Kiểm tra đoạn result có bằng đoạn substr từ 0 -> len không, nếu không thì tiếp tục giảm len để xét tiếp
            while (len > strs[i].size() || res != strs[i].substr(0, len)) {
                len--;  // Giảm len (vì không khớp)
                if (len == 0) {    // Nếu len = 0 nghĩa là 1 string nào đó không có điểm chung => empty string
                    return "";
                }
                res = res.substr(0, len);   // Giảm dần len của result để xét
            }
        }

        return res;   // return result
    }
};
```

### <span style="color: #ea580c">* Approach 2: Recursion</span>
#### Pseudo code:
```cpp
// Hàm trả về đoạn prefix giống nhau giữa 2 string
string sameSubstr(s1, s2) {
    if s1.len() > s2.len() => return sameSubstr(s2, s1)
    res = ""
    for (i := 0) -> s1.size():
        if s1[i] = s2[i] => res += s1[i]
        else: return res
    return res
}

// Hàm chia đoạn để tìm substr
string LCD(vector strs, left, right) {
    if left = right => return strs[left]

    m = (left + right) / 2
    str1 = LCD(strs, left, m)
    str2 = LCD(strs, m + 1, right)

    return sameSubstr(str1,str2)
} 

// Hàm ban đầu
string longestCommonPrefix(vector strs) {
    return LCD(strs, 0, strs.size() - 1);
}
```
#### Code:
```cpp
class Solution {
public:
    // Hàm trả về đoạn prefix giống nhau giữa 2 string
    string sameSubstr(string &s1, string &s2) {
        // Sẵn cho đoạn s1 < s2 để tính cho dễ
        if (s1.size() > s2.size()) {
            return sameSubstr(s2, s1);
        }

        string res = "";
        // Lặp từ 0 cho tới cuối, trùng nhau đến đâu thì lưu đến đó
        for (int i = 0; i < s1.size(); i++) {
            if (s1[i] == s2[i]) {
                res += s1[i];
                continue;
            }
            return res;
        }

        return res;
    }
    // Hàm chia đoạn để tìm substr
    string LCD(vector<string>& strs, int left, int right) {
        // Nếu left = right nghĩa là đang ở tại string đó => return lại chính nó
        if (left == right) {
            return strs[left];
        }

        // Tìm middle => chia để trị
        int m = (left + right) / 2;
        // str1 từ left tới m, còn str2 từ m+1 tới right vì m có khả năng ra 0, nếu để từ left -> m-1 thì sẽ error
        string str1 = LCD(strs, left, m);   // Đoạn trùng của toàn bộ string từ left -> m
        string str2 = LCD(strs, m + 1, right);  // Đoạn trùng của toàn bộ string từ m+1 -> right

        // Trả về đoạn trùng
        return sameSubstr(str1, str2);
    }

    // Hàm ban đầu
    string longestCommonPrefix(vector<string>& strs) {
        // Kết quả
        return LCD(strs, 0, strs.size() - 1);
    }
};
```

### <span style="color: #ea580c">* Approach 3: Sort vector</span>
#### Pseudo code:
```cpp
n = strs.size()

if n = 0 => return ""
if n = 1 => return strs[0]

sortAccending(strs)

if (strs[first] = strs[end]) => return strs[first]

res = ""
for (i := 0) -> strs[0].len():
    if (strs[first][i] != strs[end][i]) {
        return strs[first].substr(0, i);
    }
return strs[first]
```
#### Code:
```cpp
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int n = strs.size();   // size của vector

        if (n == 0) {
            return "";
        }
        if (n == 1) {
            return strs[0];
        }

        // Sắp xếp mảng (nó sẽ tăng dần dần theo các chữ trong mảng)
        // Các chữ cái giống nhau thì sẽ viết liền, nếu có chữ lệch đi thì sẽ nằm ở trước hoặc sau (không bao giờ nằm ở giữa các chữ giống nhau)
        // => Nên nếu ở đầu và cuối giống bao nhiêu chữ prefix thì ở giữa cũng giống vậy
        sort(strs.begin(), strs.end());   

        // Đầu cuối giống nhau thì toàn mảng giống nhau
        if (strs[0] == strs[n - 1]) {
            return strs[0];
        }

        string res = "";

        // Tìm substr
        for (int i = 0; i < strs[0].size(); i++) {
            if (strs[0][i] != strs[n - 1][i]) {
                return strs[0].substr(0, i);
            }
        }

        return strs[0];    // Nếu chuỗi đầu ngắn hơn thì đến đây return chuỗi đầu, khi qua vòng for nghĩa là toàn bộ chuỗi đầu đều nằm trong chuỗi cuối
    }
};
```