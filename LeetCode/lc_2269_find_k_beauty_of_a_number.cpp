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
    int tmp = num;
    int len = str.size();
    for (int i = len ; i >= k ; --i) {
        int divisor = pow(10, i - k);
        int substr = tmp / divisor;
        cout << substr << " ";
        if ((substr != 0) && (num % substr == 0)) {
            k_beauty_cnt++;
        }
        tmp %= int(pow(10, i - 1));
    }
    cout << endl;
    return k_beauty_cnt;
}

int main() {
    cout << divisorSubstrings(430043, 2) << endl;
}