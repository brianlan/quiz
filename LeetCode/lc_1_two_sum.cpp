#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m = unordered_map<int, int>();
        for (int i = 0 ; i < nums.size() ; ++i) {
            int gap = target - nums[i];
            if (m.find(gap) != m.end()) {
                return vector<int>{m.at(gap), i};
            } else {
                m[nums[i]] = i;
            }
        }
        return vector<int>{0, 1};
    }
};

int main(){
    std::vector<int> nums = {2,7,11,15};
    int target = 9;
    vector<int> ans = Solution().twoSum(nums, target);
    std::cout << "Final Ans: " << ans[0] << ", " << ans[1] << std::endl;
}