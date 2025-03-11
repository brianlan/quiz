#include <iostream>
#include <stack>
#include <string>
#include <map>
using namespace std;


bool isValid(string s) {
    if (s.size() % 2 != 0) return false;
    stack<char> validator;
    map<char, char> peer = {{')', '('}, {']', '['}, {'}', '{'}};
    for (const auto& c : s) {
        if (c == '(' || c == '[' || c == '{') {
            validator.push(c);
        } else {
            if (validator.empty() || peer[c] != validator.top()) return false;
            validator.pop();
        }
    }
    if (validator.empty()) return true;
    return false;
}

int main() {
    string s = "((";
    cout << isValid(s) << endl; 
}