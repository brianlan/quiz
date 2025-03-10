#include <iostream>
#include <string>
#include <cmath>

using namespace std;


int divisorSubstrings(int num, int k) {
    if (num < 10) {
        return 1;
    }
    int k_beauty_cnt = 0;
    string str = to_string(num);
    int len = str.size();
    for (int i = len ; i >= k ; --i) {
        int divisor = pow(10, i - k);
        if (num % (num / divisor) == 0) {
            k_beauty_cnt++;
        }
        num /= 10;
    }
    return k_beauty_cnt;
}

int main() {
    cout << divisorSubstrings(430043, 2) << endl;
}