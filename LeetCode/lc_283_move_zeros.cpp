/* 
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1


Follow up: Could you minimize the total number of operations done?
*/
#include <iostream>
#include <vector>

using namespace std;


class Solution {
public: 
    void moveZeros(vector<int>& nums) {
        /*
        1, 2, 0, 3, 0, 4, 5, 0, 0, 6 (i=0, left=0 => i=1, left=1)
        1, 2, 0, 3, 0, 4, 5, 0, 0, 6 (i=1, left=1 => i=2, left=2)
        1, 2, 0, 3, 0, 4, 5, 0, 0, 6 (i=2, left=2 => i=3, left=3)
        1, 2, 3, 0, 0, 4, 5, 0, 0, 6 (i=3, left=3 => i=4, left=3)
        1, 2, 3, 0, 0, 4, 5, 0, 0, 6 (i=4, left=3 => i=5, left=4)
        1, 2, 3, 4, 0, 0, 5, 0, 0, 6 (i=5, left=4 => i=6, left=5)
        1, 2, 3, 4, 5, 0, 0, 0, 0, 6 (i=6, left=5 => i=7, left=5)
        1, 2, 3, 4, 5, 0, 0, 0, 0, 6 (i=7, left=5 => i=8, left=5)
        1, 2, 3, 4, 5, 6, 0, 0, 0, 0 (i=8, left=5 => i=9, left=6)
        */
        int n = nums.size();
        int left = 0;
        auto exchange = [&](int p, int q) { auto tmp = nums[p]; nums[p] = nums[q]; nums[q] = tmp; };
        for (int i = 0 ; i < n - 1 ; ++i) {
            if (nums[i] != 0) { // including cases like: 1, 2 and 3, 0
                ++left;
            } else {
                if (nums[i + 1] != 0) { // e.g. 0, 1
                    exchange(left, i + 1);
                    ++left;
                }
            }
        }
    }
};


int main() {
    vector<int> nums = {1, 2, 0, 3, 0, 4, 5, 0, 0, 6};
    // vector<int> nums = {0, 1, 2, 3, 4, 0, 5, 6, 7, 0};
    Solution().moveZeros(nums);
    for (const auto& num : nums) {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}