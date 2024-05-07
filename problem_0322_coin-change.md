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

### <span style="color: #ea580c">* Approach 1: Đệ quy (Tìm toàn bộ tất cả TH) (TIME LIMIT ERROR)</span>
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

### <span style="color: #ea580c">* Approach 2: Đệ quy (lưu giữ giá trị bằng mảng)</span>
#### Những ý cần giải thích

*(Hiểu được bản chất ở trên thì sẽ bài này sẽ dễ hiểu hơn)*
- Ý tưởng: Dùng đệ quy và mỗi lần tính được số coin ít nhất để tạo ra một coin khác thì lưu vào mảng để nếu sau khi gặp lại thì nó tự động return giá trị đã tính nên không phải tính lại từ đầu.
- Giải thích mảng dp:
  - Nếu **= INT_MAX** nghĩa là không có số coin hợp lệ để tạo ra coin có giá trị đó.
  - Nếu **= -1** nghĩa là coin đó chưa được tính (nên tiếp tục tính cái đó).
  - Nếu **= một giá trị nào đó** thì đó là min coin để tạo ra coin có giá trị đó.


#### Pseudo code:
```cpp
function minNumOfCoins(coins, amount, dp) {
    if (amount = 0) => return 0     // Có 0 coin để tạo ra giá trị 0
    if (amount < 0) => return INT_MAX  // Không hợp lệ
    if (dp[amount] != -1) => return dp[amount]   // != -1 nghĩa là đã được tính nên return lại giá trị luôn mà không cần tính lại

    minCount = INT_MAX
    for (i := 0) -> coins.size():
        count = minNumOfCoins(coins, amount - coins[i], dp)
        if (minCount != INT_MAX):      // Nếu min(INT_MAX, INT_MAX) sẽ bị lỗi nên để tránh trường hợp bị lỗi
            minCount = min(minCount, count + 1)   // Count + 1 vì count chỉ là số coin để tạo ra amount - coins[i], phải +1 do thêm coin là coins[i] thì mới là số coin để tạo amount

    dp[amount] = amount   // Số coin ít nhất cần để tạo thành amount là minCount
    return amount
}

function coinChange(coins, amount) {
    vector dp (có size amount + 1 với toàn bộ giá trị -1)

    res = minNumOfCoins(coins, amount, dp)

    if (res == INT_MAX) -> return -1   // Nếu res = INT_MAX nghĩa là không có giá trị hợp lệ
    else: return res
}
```
#### Code:
```cpp
class Solution {
public:
    int minNumOfCoins(vector<int>&coins, int amount, vector<int>& dp) {
        if (amount == 0) {   // Có 0 coin để tạo ra giá trị 0
            return 0;
        }

        if (amount < 0) {    // Không hợp lệ
            return INT_MAX;
        }

        if (dp[amount] != -1) {   // != -1 nghĩa là đã được tính nên return lại giá trị luôn mà không cần tính lại
            return dp[amount];
        }

        int minCount = INT_MAX;    // Biến lưu min số coin cần để = amount
        for (int i = 0; i < coins.size(); i++) {
            int count = minNumOfCoins(coins, amount - coins[i], dp);   // Tìm số coin để tạo ra amount - coins[i]
            if (count != INT_MAX) {   // Nếu min(INT_MAX, INT_MAX) sẽ bị lỗi nên để tránh trường hợp bị lỗi
                minCount = min(minCount, count + 1);     // Count + 1 vì count chỉ là số coin để tạo ra amount - coins[i], phải +1 do thêm coin là coins[i] thì mới là số coin để tạo amount
            }
        }

        dp[amount] = minCount;   // Số coin ít nhất cần để tạo thành amount là minCount
        return minCount;
    }

    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount + 1, -1);   // Tạo mảng dp với size là amount + 1, toàn bộ giá trị là -1

        int res = minNumOfCoins(coins, amount, dp);  

        if (res == INT_MAX) {     // Nếu res = INT_MAX nghĩa là không có giá trị hợp lệ
            return -1;
        }
        return res;
    }
};
```

### <span style="color: #ea580c">* Approach 3: Dynamic programming</span>
#### Pseudo code:
```cpp
vector dp (có size amount + 1 với toàn bộ giá trị -1)
dp[0] = 0
for (i := 1) => amount:
    for (j := 0) -> coins.size():
        resValue = i - coins[j]
        if (resValue >= 0) and (dp[resValue] có giá trị):
            dp[i] = min(dp[i], dp[resValue] + 1)

if (dp[amount] = INT_MAX) => return -1

return dp[amount]
```
#### Code:
```cpp
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount + 1, INT_MAX);   // Một mảng chứa số coin ít nhất cần phải có để tạo thành index của nó (INT_MAX là không có cách)
        dp[0] = 0;    // Xử lí trường hợp amount = 0
        for (int i = 1; i <= amount; i++) {    // Lặp hết các số đến amount để tìm hết số coin min của từng số
            for (int j = 0; j < coins.size(); j++) {   // Xét trường hợp coins[j] là coin đầu tiên thì số coin min để tạo ra i là bn.
                int residualValue = i - coins[j];    // Giá trị còn lại khi đã có coin đầu tiên là coins[j]
                if (residualValue >= 0 && dp[residualValue] != INT_MAX) {   // Nếu giá trị đó >= 0 và phải tồn tại cách để tạo ra nó thì mới xét min
                    dp[i] = min(dp[i], dp[residualValue] + 1);
                }
            }
        }

        // Nếu dp[amount] = INT_MAX thì nghĩa là không tồn tại cách để tạo ra amount
        if (dp[amount] == INT_MAX) return -1;

        return dp[amount];
    }
};
```