# <span style="color: #f43f5e" >13. Roman to integer</span>

## <span style="color: #10b981">Description:</span>
**Link:** https://leetcode.com/problems/roman-to-integer/description/
Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.
```
Symbol       Value
I            1
V            5
X            10
L            50
C            100
D            500
M            1000
```
For example, 2 is written as `II` in Roman numeral, just two ones added together. 12 is written as `XII`, which is simply `X` + `II`. The number 27 is written as `XXVII`, which is `XX` + `V` + `II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

- `I` can be placed before `V` (5) and `X` (10) to make 4 and 9. 
- `X` can be placed before `L` (50) and `C` (100) to make 40 and 90. 
- `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

## <span style="color: #10b981">Solution:</span>

### <span style="color: #ea580c">* Approach 1: Map and brute force</span>
#### Pseudo code:
```cpp
map<char, int> mp;
mp['I'] = 1;
mp['V'] = 5;
mp['X'] = 10;
mp['L'] = 50;
mp['C'] = 100;
mp['D'] = 500;
mp['M'] = 1000;

int result = 0;

for (i := 0) -> s.len():
    if mp[s[i]] < mp[s[i + 1]] => result -= mp[s[i]]
    else: result += mp[i]

return result

```
#### Code:
```cpp
class Solution {
public:
    int romanToInt(string s) {
        map<char, int> mp;
        mp['I'] = 1;
        mp['V'] = 5;
        mp['X'] = 10;
        mp['L'] = 50;
        mp['C'] = 100;
        mp['D'] = 500;
        mp['M'] = 1000;

        int result = 0;  // Biến lưu trữ kết quả
    

        for(int i = 0; i < s.length(); i++){
            if (mp[s[i]] < mp[s[i + 1]]) {
                // Nếu kí tự trước nhỏ hơn kí tự sau thì chắc chắn sẽ bị trừ đi. Ví dụ như XIV, I ở giữ sẽ bị trừ đi vì nhỏ hơn V
                result -= mp[s[i]];
            }
            else {
                // Còn lại thì nếu nó tăng dần thì sẽ cộng vào
                // Trường hợp = nhau thì thì sẽ vẫn cộng
                // Không cần lo trường hợp giống nhau và bị trừ vì IIV không tồn tại, chỉ có IV.
                result += mp[s[i]]
            };
        }

        return result;    // Trả lại giá trị
    }
};
```

### <span style="color: #ea580c">* Approach 2: If else</span>
#### Pseudo code:
```cpp
sum = 0
for (i := 0) -> s.len():
    switch(s[i]):
        case 'I', 'X', 'C':
            if (s[i + 1] = những char lớn hơn mà có thể đặt trước) {
                sum -= value of s[i]
                break
            }

            sum += value of s[i]

        case 'V', 'L', 'D', 'M':
            sum += value of s[i]
```
#### Code:
```cpp
class Solution {
public:
    int romanToInt(string s) {
        int sum = 0;

        // Lặp từng giá trị trong s
        for (int i = 0; i < s.length(); i++) {
            // Kiểm tra gặp char nào
            switch(s[i]) {
                case 'I':
                    // Trước I là V và X thì sẽ -1, còn không thì +1
                    if (s[i + 1] == 'V'  s[i + 1] == 'X') {
                        sum -= 1;
                        break;
                    }

                    sum += 1;
                    break;
                // Trước X là L và C thì sẽ -10, còn không thì +10
                case 'X':
                    if (s[i + 1] == 'L'  s[i + 1] == 'C') {
                        sum -= 10;
                        break;
                    }

                    sum += 10;
                    break;
                // Trước C là D và M thì sẽ -100, còn không thì +100
                case 'C':
                    if (s[i + 1] == 'D'  s[i + 1] == 'M') {
                        sum -= 100;
                        break;
                    }

                    sum += 100;
                    break;
                // Các trường hợp còn lại thì cộng với giá trị tương ứng
                case 'V':
                    sum += 5;
                    break;
                case 'L':
                    sum += 50;
                    break;
                case 'D':
                    sum += 500;
                    break;
                case 'M':
                    sum += 1000;
                    break;
            }
        }

        return sum;
    }
};
```

### <span style="color: #ea580c">* Approach 3: Regex</span>
#### Pseudo code:
```cpp
s = s.replaceAll("IV" -> "IIII")
s = s.replaceAll("IX" -> "VIIII")
s = s.replaceAll("XL" -> "XXXX")
s = s.replaceAll("XC" -> "LXXXX")
s = s.replaceAll("CD" -> "CCCC")
s = s.replaceAll("CM" -> "DCCCC")

map<char, int> mp;
mp['I'] = 1;
mp['V'] = 5;
mp['X'] = 10;
mp['L'] = 50;
mp['C'] = 100;
mp['D'] = 500;
mp['M'] = 1000;

int sum = 0;

for (i := 0) -> len(s):
    sum += mp[s[i]]

return sum
```
#### Code:
```cpp
class Solution {
public:
    int romanToInt(string s) {
        // Thay hết các trường hợp mà số bị giảm đi do nằm bên trái số lớn hơn nó bằng các số để cộng vào
        s = regex_replace(s, regex("IV"), "IIII");
        s = regex_replace(s, regex("IX"), "VIIII");
        s = regex_replace(s, regex("XL"), "XXXX");
        s = regex_replace(s, regex("XC"), "LXXXX");
        s = regex_replace(s, regex("CD"), "CCCC");
        s = regex_replace(s, regex("CM"), "DCCCC");

        // Tạo map chứa giá trị của từng char
        unordered_map<char, int> mp;
        mp['I'] = 1;
        mp['V'] = 5;
        mp['X'] = 10;
        mp['L'] = 50;
        mp['C'] = 100;
        mp['D'] = 500;
        mp['M'] = 1000;

        int sum = 0;   // Biến để lưu trữ giá trị

        // Lặp hết các char trong string và cộng giá trị tương ứng với mỗi char
        for (auto cha : s) {
            sum += mp[cha];
        }

        return sum;
    }
};
```