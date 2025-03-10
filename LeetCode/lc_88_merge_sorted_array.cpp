#include <iostream>
#include <vector>
using namespace std;

void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    if (m == 0) {
        for (int i = 0 ; i < n ; ++i){
            nums1[i] = nums2[i];
        }
        return;
    }
    if (n == 0) {
        return;
    }
    vector<int> trueNums1 = vector<int>(nums1.begin(), nums1.begin() + m);
    int p = 0, q = 0, i = 0;
    while (p < m && q < n) {
        if (trueNums1[p] <= nums2[q]) {
            nums1[i] = trueNums1[p];
            p++;
        } else {
            nums1[i] = nums2[q];
            q++;
        }
        ++i;
    }
    if (p == m) {
        for (vector<int>::iterator it = nums2.begin() + q ; it != nums2.end() ; ++it) {
            nums1[i] = *it;
        }
    } else { // q == n
        for (vector<int>::iterator it = trueNums1.begin() + p ; it != trueNums1.end() ; ++it) {
            nums1[i] = *it;
        }
    }
}

int main() {
    vector<int> nums1 = {1, 2, 3, 0, 0, 0};
    vector<int> nums2 = {2, 5, 6};
    merge(nums1, 3, nums2, 3);
    for(const auto& v: nums1) {
        cout << v << endl;
    }
}