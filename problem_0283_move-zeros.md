# <span style="color: #f43f5e" >283. Move Zeros</span>

## <span style="color: #10b981">Description:</span>
**Link:** https://leetcode.com/problems/move-zeroes/description/

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

**Example 1:**
```cpp
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```
**Example 2:**
```cpp
Input: nums = [0]
Output: [0]
```

**Constraints:**
```cpp
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
```

Follow up: Could you minimize the total number of operations done?

## <span style="color: #10b981">Solution:</span>

### <span style="color: #ea580c">* Approach 1: Two pointers</span>
#### Pseudo code:
- **Ý tưởng** : Dùng 2 con trỏ, mỗi lần gặp số != 0 thì tại vị trí lastNotZero sẽ thay bằng giá trị đó, và sau đó tiếp tục tăng lên vị trí tiếp theo, tiếp diễn cho tới khi hết mảng, lastNotZero đồng thời cũng là số phần tử khác 0, nên cho giá trị từ vị trí lastNotZero tới cuối bằng 0
```cpp
lastNotZero = 0
FOR (i := 0) -> nums.size():
    IF nums[i] != 0 THEN:
        nums[lasNotZero] = nums[i]
        lastNotZero++

Gán giá trị từ lastNotZero tới cuối = 0
```
#### Code:
```cpp
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int lastNotZero = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != 0) {
                nums[lastNotZero] = nums[i];
                lastNotZero++;
            }
        }

        fill(nums.begin() + lastNotZero, nums.end(), 0);
    }
};
```

### <span style="color: #ea580c">* Approach 2: Stable sort</span>
#### Pseudo code:
- **Ý tưởng**: Xài stable sort để cho 0 về cuối mảng, chỉ khi trường hợp a != 0 và b = 0 thì mới không đảo, còn lại sẽ bị đảo hết.
#### Code:
```cpp
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        stable_sort(nums.begin(), nums.end(), [](int a, int b) -> bool {
            return a != 0 && b == 0;
        });
    }
};
```

### <span style="color: #ea580c">* Approach 3: Stable partition</span>
#### Pseudo code:
- **Ý tưởng**: Xài stable partition, giá trị true sẽ đứng trước, giá trị false đứng sau, các giá trị được sắp xếp không đổi trật tự đứng.
#### Code:
```cpp
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        stable_partition(nums.begin(), nums.end(), [](int num) -> bool {
            return num != 0;
        });
    }
};
```