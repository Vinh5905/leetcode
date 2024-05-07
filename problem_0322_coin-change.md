# <span style="color: #f43f5e" >322. Coin Change</span>

## <span style="color: #10b981">Description:</span>
**Link:** https://leetcode.com/problems/coin-change/description/

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.

 

**Example 1:**
```cpp
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```
**Example 2:**
```cpp
Input: coins = [2], amount = 3
Output: -1
```
**Example 3:**
```cpp
Input: coins = [1], amount = 0
Output: 0
```

**Constraints:**
```cpp
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
```


## <span style="color: #10b981">Solution:</span>

### <span style="color: #ea580c">* Approach 1: Đệ quy (TIME LIMIT ERROR)</span>
#### Pseudo code:
```cpp

```
#### Code:
```cpp
class Solution {
public:
    int countCoin(vector<int>& coins, int amount, int currentSum, int count, int index) {
        if (currentSum > amount) {   // Nếu vượt quá thì coi như không dãy giá trị đó không được nên return 0
            return 0;
        } else if (currentSum == amount) {   // Nếu bằng nghĩa là được thì return lại số lượng coin cần để tạo currentSum.
            return count;
        }

        int minCount = INT_MAX;   // Biến lưu giá trị nhỏ nhất mỗi lần đệ quy
        // Với mỗi một currentSum đang xét thì kiểm tra hết toàn bộ giá trị có thể đi cùng
        for (int i = 0; i < index; i++) {
            int minOfi = countCoin(coins, amount, currentSum + coins[i], count + 1, i + 1);
            if (minOfi != 0) {
                minCount = min(minCount, minOfi);   // Tìm min cho mỗi lần xét với giá trị coins[i]
            } 
        }

        // Nếu minCount không thay đổi nghĩa là không tất cả TH đó không có TH nào cho ra tổng bằng amount.
        if (minCount == INT_MAX) {
            return 0;
        }

        return minCount;
    }

    int coinChange(vector<int>& coins, int amount) {
        sort(coins.begin(), coins.end());   // Sắp xếp coin tăng dần (cũng không có ý nghĩa lắm ngoài việc cho nó dễ hiểu hơn)

        if (!amount) return 0;

        int count = countCoin(coins, amount, 0, 0, coins.size());
        if (count) {
            return count;
        }
        return -1;
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