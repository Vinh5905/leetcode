# <span style="color: #f43f5e" >74. Search a 2D Matrix</span>

## <span style="color: #10b981">Description:</span>
**Link:** https://leetcode.com/problems/search-a-2d-matrix/description/

You are given an `m x n` integer matrix matrix with the following two properties:

Each row is sorted in **non-decreasing order**.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in **O(log(m * n))** time complexity.


**Example 1:**
```cpp
Input: matrix = [
    [1  3  5  7 ]
    [10 11 16 20]
    [23 30 34 60]
]
, target = 3
Output: true
```
**Example 2:**
```cpp
Input: matrix = [
    [1  3  5  7 ]
    [10 11 16 20]
    [23 30 34 60]
]
, target = 13
Output: false
```
 
**Constraints:**
```cpp
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
```


## <span style="color: #10b981">Solution:</span>

### <span style="color: #ea580c">* Approach 1: Find row and use binary search</span>
#### Pseudo code:
```cpp
if (first value of matrix > target) or (last value of matrix < target) => return false
indexRow = 0

for (i := 1) -> matrix.size():
    if (first value of matrix[i] <= target) => indexRow = index of that row
    else: break

bool find = binary_search(matrix, target)
return find
```
#### Code:
```cpp
class Solution {
public:

    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // Giá trị đầu tiên và cuối cùng của matrix lần lượt là giá trị nhỏ nhất và lớn nhất của matrix, nếu target không nằm vượt ngoài phạm vi này thì sẽ không nằm trong matrix => false
        if (matrix[0][0] > target || matrix[matrix.size() - 1][matrix[0].size() - 1] < target) {
            return false;
        }

        int indexRow = 0;   // index của row có thể chứa target
        for (int i = 1; i < matrix.size(); i++) {
            if (matrix[i][0] <= target) {
                // Nếu value đầu của row nhỏ hơn target thì có thể target nằm trong row nên lưu row đó lại.
                // Tiếp tục xét cho tới khi giá trị đầu của row nào đó lớn hơn target thì chắc chắc target chỉ có thể nằm ở row trước đó.
                indexRow = i;
            } else {
                break;
            }
        }

        // Dùng binary search để tìm kiếm target trong row (vì dãy tăng dần)
        bool find = binary_search(matrix[indexRow].begin(), matrix[indexRow].end(), target);
        return find;
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