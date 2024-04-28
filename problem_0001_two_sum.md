# <span style="color: #f43f5e" >1. Two sum</span>

## <span style="color: #10b981">Description:</span>
**Link:** https://leetcode.com/problems/two-sum/description/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
 

**Example 1:**
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3:**
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

**Constraints:**
```
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
```
Only one valid answer exists.

## <span style="color: #10b981">Solution:</span>

### <span style="color: #ea580c">* Approach 1: Brute force</span>
#### Pseudo code:
```cpp
for (i := 0) -> n:
    for (j := i + 1) -> n:
        if (a[i] + a[j] = target) => return {i, j}

return {}
```

#### Code:
```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size() - 1; i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[i] + nums[j] == target) {
                    return {i, j};
                }
            }
        }

        return {};
    }
};
```


### <span style="color: #ea580c">* Approach 2: Hash table</span>
#### Pseudo code:
```cpp
class MyHashTable {
private:
    size = 100
    vector< vector<pair<index, key>> > arr
    function myHashFunction(int key) {
        return (abs(key) % size);
    }

public:
    HashTable() {
        arr.resize(size);
    }

    void add(index, key) {
    // Add pair<index, key> vào bucket
    }

    int findValueNotIndex(int index, key) {
          // Tìm kiếm một pair thỏa mãn:
          // = key và != index (không bị trùng lặp)
          // Có thì return index, không thì return -1
	}
}

=> Trong hàm solution:

MyHashTable container;   // Khởi tạo đối tượng

for (i := 0) -> nums.size():
    container.add(i, nums[i])  // (index, key)

for (i := 0) -> nums.size():
    index = container.findValueNotIndex(i, target - nums[i]);

    if (nums[i] != 0) => return {i, index};

return {}   // Nếu không tồn tại
```

#### Code:
```cpp
// Xây dựng class hash table
class MyHashTable {
private:
    int mySize = 100;
    vector<vector<pair<int, int>>> container;
    int myHashFunction(int key) {
        return (abs(key) % mySize);
    }

public:
    MyHashTable() {
        container.resize(mySize);
    }

    void add(int &index, int &key) {
        int indexInHash = myHashFunction(key);
        vector<pair<int, int>> &bucket = container[indexInHash];
        bucket.push_back(make_pair(index, key));
    }

    int findValueNotIndex(int index, int key) {
        int indexInHash = myHashFunction(key);
        vector<pair<int, int>> &bucket = container[indexInHash];

        for (auto &ele : bucket) {
            if (ele.second == key && ele.first != index) {
                return ele.first;
            }
        }

        return -1;
    }
};

// solution
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        MyHashTable hashContain;   // Khai báo đối tượng

        for (int i  = 0; i < nums.size(); i++) {
            hashContain.add(i, nums[i]);   // Cho từng cặp pair<index, key> vào trong hash table
        }

        for (int i = 0; i < nums.size(); i++) {    // Lặp từng phần tử
            int index = hashContain.findValueNotIndex(i, target - nums[i]);    // Tìm trong hash table có tồn tại phần tử + nums[i] = target không
            if (index != -1) {
                return {i, index};   // Chắn chắn đã được sắp xếp theo thứ tự i < index
            }
        }

        return {};  // Nếu không tồn tại
    }
};
```

### <span style="color: #ea580c">* Approach 3: Two  pointers</span>
#### Pseudo code:
```cpp
bool cmp(pair a, pair b) {
    return a.key < b.key;
}

=> Trong hàm solution:
vector<int, int> v;
for (i := 0) -> nums.size() {
    v.push({value, key})
}

sort(v.begin(), v.end(), cmp)

i = 0; j = v.size() - 1;

while (i < j):
    if (v[i].key + v[j].key = target):
        if (v[i].index <= v[j].index) => return {i, j}
        if (v[i].index > v[j].index) => return {j, i}
    else:
        if (v[i].key + v[j].key < target): i++
        else: j--
return {}
```

#### Code:
```cpp
bool cmp(pair<int, int> a, pair<int, int> b){
    return a.first < b.first;     // Hàm so sánh (tăng dần)
}

class Solution{
public:
    vector<int> twoSum(vector<int>& nums, int target){
        vector<pair<int, int>> v;
        for(int i = 0; i < nums.size(); i++){
            v.push_back({nums[i], i});     // Push vào vector dưới dạng (value, key)
        }
        sort(v.begin(), v.end(), cmp);   // Sắp xếp tăng dần theo value
        int i = 0, j = v.size() - 1;     // 2 con trỏ chạy 2 đầu
        while(i < j){
            if(v[i].first + v[j].first == target){
                // Nếu bằng thì muốn return ra {i, j} với i < j cần so sánh index nào trước
                if(v[i].second < v[j].second) return{v[i].second, v[j].second};
                else return{v[j].second, v[i].second}
            }
            else if(v[i].first + v[j].first < target) i++;   // Nếu nhỏ hơn target nghĩa là cần tăng thêm giá trị => tăng i
            else j--;    // Giá trị quá lớn cần giảm xuống => tăng j
        }
        return {};
    }
};
```
