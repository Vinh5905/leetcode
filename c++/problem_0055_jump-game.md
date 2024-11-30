# <span style="color: #f43f5e" >55. Jump Game</span>

## <span style="color: #10b981">Description:</span>
**Link:** https://leetcode.com/problems/jump-game/description/

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return `true` *if you can reach the last index*, *or* `false` *otherwise.*

**Example 1:**
```cpp
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Example 2:**
```cpp
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. 
Its maximum jump length is 0, which makes it impossible to reach the last index.
```

**Constraints:**
```cpp
1 <= nums.length <= 104
0 <= nums[i] <= 105
```

## <span style="color: #10b981">Solution:</span>

### <span style="color: #ea580c">* Approach 1: Dynamic programming</span>
#### Những ý cần giải thích
- **Ý tưởng**: Xét ngược từ dưới lên tìm xem vị trí ở mỗi phần tử có khả năng đi đến cuối được không. *(lần tính càng về sau thì sẽ sử dụng những vị trí đã được xác định sẵn là có thể đến đích hay không nên sẽ không cần tính lại)*


#### Pseudo code:
```cpp
n = nums.size()
vector check(n phần tử false);

check[last] = true;
for (i := n - 2) => 0:
    Chạy hết các vị trí có khả năng của nums[i] :
        if vị trí đó true:
            check[i] = true
            break
return check[first]
```
#### Code:
```cpp
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        vector<bool> check(n, false);   // Tạo mảng toàn false chứa khả năng đến đích được của từng giá trị nums[i] (theo index của nums[i])

        check[n - 1] = true;   // Giá trị cuối cùng là giá trị đích nên true
        for (int i = n - 2; i >= 0; i--) {   // Chạy từ giá trị n - 2 cho tới cuối
            for (int j = 1; j <= nums[i] && i + j < n; j++) {  // Xét hết trường hợp có thể chạy của nums[i]
                if (check[i + j]) {   // Nếu tại vị trí đó là true (nghĩa là tại vị trí đó có thể đi được đến đích => vị trí hiện tại cũng đến được đích)
                    check[i] = true;
                    break;
                }
            }
        }
        
        return check[0];   // Trả về giá trị đầu tiên xem có thể đến đích không
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