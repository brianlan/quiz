#include <iostream>
#include <set>
#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> getDigits(int n) const {
        vector<int> digits;
        while (n >= 10) {
            int digit = n % 10;
            if (digit != 0) {
                digits.push_back(n % 10);
            }
            n /= 10;
        }
        digits.push_back(n);
        return digits;
    }
    
    int getSquareSum(vector<int>& digits) {
        int sum = 0;
        for (const auto& d : digits) {
            sum += d * d;
        }
        return sum;
    }

    bool isHappy(int n) {
        unordered_set<int> seen;
        seen.insert(n);
        while (n != 1) {
            vector<int> digits = getDigits(n);
            int sum = getSquareSum(digits);
            if (seen.find(sum) != seen.end()) {
                return false;
            }
            seen.insert(sum);
            n = sum;
        }

        return true;
    }
};


int main() {
    unique_ptr<Solution> solution = make_unique<Solution>();
    cout << solution->isHappy(2) << endl;
}