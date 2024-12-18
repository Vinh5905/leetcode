# <span style="color: #f43f5e" >79. Word Search</span>

## <span style="color: #10b981">Description:</span>
**Link:** https://leetcode.com/problems/word-search/

Given an `m x n` grid of characters `board` and a string `word`, return **true** if *word exists in the grid*.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

**Example 1:**
![image](/c++/picture/word-search-1.jpeg)
```cpp
Input: 
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
Output: true
```

**Example 2:**
![image](/c++/picture/word-search-2.jpeg)
```cpp
Input: 
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "SEE"
Output: true
```

**Example 3:**
![image](/c++/picture/word-search-3.jpeg)
```cpp
Input: 
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCB"
Output: false
```

**Constraints:**
```cpp
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
```

Follow up: Could you use search pruning to make your solution faster with a larger board?



## <span style="color: #10b981">Solution:</span>

### <span style="color: #ea580c">* Approach 1: Recursion (backtrack)</span>
#### Pseudo code:

- **Ý tưởng**: Dùng recursion, mỗi lần chạy kiểm tra char đầu tiên, nếu thấy char đầu tiên khớp thì bắt đầu recursion chạy xung quanh 4 phía để kiểm ra (mỗi lần kiểm tra đoạn nào thì sẽ đặt giá trị là một char k thể có, để phân biệt đường đã đi, sau khi bị false thì quay trở về giá trị ban đầu của nó)

```cpp

// 4 góc xung quanh (kĩ thuật loang trên mảng 2 chiều)
rows[4] = {-1, 0, 1, 0};
cols[4] = {0, 1, 0, -1};

function backTracking(int row, int col, vector<vector<char>> &board, string word, int index):
    IF (row or col ra vượt index của board) THEN return false

    IF (word[index] != board[row][col]) THEN return false
    ELSE: (
        IF (index == last char of word) THEN return true
    )

    char temp = board[row][col];
    board[row][col] = '\0';

    FOR (i := 0) -> 4:
        // Vị trí tiếp theo
        newRow = row + rows[i]
        newCol = col + cols[i]

        IF {row, col} not found in path THEN:
            IF (backTracking(newRow, newCol, board, word, index + 1)) THEN return true

    board[row][col] = temp; // false nên sửa lại giá trị ban đầu

    return false;
        

function exist(vector<vector<char>>& board, string word):
    FOR (i := 0) -> board.size():
        FOR (j := 0) -> board[0].size():
            if (backTracking(i, j, board, word, 0)) THEN return true

    return false
```
#### Code:
```cpp
int rows[4] = {-1, 0, 1, 0};
int cols[4] = {0, 1, 0, -1};

class Solution {
public:
    bool backTracking(int row, int col, vector<vector<char>>& board, string word, int index) {
        // Giá trị row và col vượt khỏi mảng thì coi như false
        if (row < 0 || row >= board.size() || col < 0 || col >= board[0].size()) {
            return false;
        }

        // Nếu giá trị ở index đang xét khác với char trong board đang xét thì false 
        if (word[index] != board[row][col]) {
            return false;
        } else {
            // Nếu bằng nhau và là char cuối cùng thì true luôn
            if (index == word.size() - 1) {
                return true;
            }
        }

        // Lưu lại giá trị đã đi qua, để không bị trùng lặp thì thay thế nó bằng giá trị mà trong string không có.
        char temp = board[row][col];
        board[row][col] = '\0';

        // Tìm cả 4 hướng
        for (int i = 0; i < 4; i++) {
            int newRow = row + rows[i];
            int newCol = col + cols[i];

            if (backTracking(newRow, newCol, board, word, index + 1)) {
                return true;
            }
        }
        // Thay lại giá trị để xét hướng khác không bị ảnh hưởng
        board[row][col] = temp;

        return false;
    }

    bool exist(vector<vector<char>>& board, string word) {

        // Chạy hết mảng board
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[i].size(); j++) {
                if (backTracking(i, j, board, word, 0)) {
                    return true;
                }
            }
        }

        return false;
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