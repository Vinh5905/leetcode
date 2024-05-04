# <span style="color: #f43f5e" >75. Sort Colors</span>

## <span style="color: #10b981">Description:</span>
**Link:** https://leetcode.com/problems/sort-colors/description/

Given an array nums with n objects colored red, white, or blue, sort them **in-place** so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

You must solve this problem **without using the library's sort function**.

 

**Example 1:**
```cpp
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```
**Example 2:**
```cpp
Input: nums = [2,0,1]
Output: [0,1,2]
```
**Constraints:**
```cpp
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
```

## <span style="color: #10b981">Solution:</span>

### <span style="color: #ea580c">* Approach 1: Dutch National Flag algorithm</span>
#### Pseudo code:
```cpp
start = 0
end = nums.size() - 1
mid = 0
while mid <= end:
    if nums[mid]:
        = 0:
            swap(nums[start] với nums[mid])
            start++; mid++;
        = 1:
            mid++
        = 2:
            swap(nums[mid] với nums[end])
            end--
```
#### Code:
```cpp
class Solution {
public:
    void sortColors(vector<int>& nums) {
        // Xét 3 con trỏ
        int start = 0, mid = 0, end = nums.size() - 1;
        
        while (mid <= end) {   // Dừng lại khi mid vượt quá end (tất cả giá trị đã đúng vị trí)
            switch (nums[mid]) {     // Xét biến mid
                case 0:
                    // Nếu = 0 => swap start với mid, sau đó tăng start, mid
                    // Khi ở đầu đang là 0 0 0 thì nó sẽ chạy qua hết tất cả, đến khi gặp một giá trị khác thì sẽ chạy xuống các TH dưới
                    swap(nums[start], nums[mid]);
                    start++, mid++;
                    break;
                case 1:
                    // Nếu = 1 thì bỏ qua tiếp tục tìm giá trị != 1 để xét
                    mid++;
                    break;
                case 2:
                    // Nếu = 2 thì sẽ swap mid và end, sau đó giảm end
                    // Mục đích là để giữ nguyên mid trong trường hợp giá trị mid bị swap khác đi thì nó sẽ xét TH mid bị thay đổi đó (nên mới không tăng mid)
                    // Nếu giá trị sau khi swap = 2 thì nghĩa là số ở end đã đúng nên nó giảm tiếp đi và xét tới khi nào end != 2 để thay đổi mid và tiếp tục các TH khác
                    swap(nums[mid], nums[end]);
                    end--;
                    break;
            }
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