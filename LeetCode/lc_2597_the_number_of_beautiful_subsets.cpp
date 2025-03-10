#include <iostream>
#include <vector>
#include <bit>


int bit_count(int value) {
    int count = 0;
    while (value) {
        count += value & 1; // Check if the least significant bit is set
        value >>= 1; // Shift right by 1 bit
    }
    return count;
}


int beautifulSubsets(std::vector<int>& nums, int k) {
    int n = nums.size();
    int ans = n; // single element sets are all beautiful.
    std::vector<int> exclusive_pairs;
    for (int i = 0 ; i < n ; ++i) {
        for (int j = i; j < n ; ++j) {
            if (abs(nums[i] - nums[j]) == k) {
                std::cout << "i=" << i << " " << (1 << i) << ",  j=" << j << " " << (1 << j) << std::endl;
                exclusive_pairs.push_back((1 << i) | (1 << j));
            }
        }
    }
    for (auto& v : exclusive_pairs) std::cout << v << std::endl;
    for (int i = 1 ; i < (1 << n) ; ++i) {
        if (bit_count(i) < 2) {
            continue;
        }
        bool containsExclusivePair = false;
        for (const auto& pair : exclusive_pairs) {
            if ((i & pair) == pair) {
                containsExclusivePair = true;
                break;
            }
        }
        if (!containsExclusivePair) {
            ans++;
        }
    }
    return ans;
}

int main(){
    std::vector<int> nums = {4,2,5,9,10};
    int k = 1;
    int ans = beautifulSubsets(nums, k);
    std::cout << "Final Ans: " << ans << std::endl;
}