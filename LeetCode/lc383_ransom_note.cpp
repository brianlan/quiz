#include <iostream>
#include <map>
#include <string>

using namespace std;

void buildStats(const string& str, map<char, int>& stats) {
    for (const auto& c: str) {
        stats[c]++;
    }
}

bool canConstruct(string ransomNote, string magazine) {
    map<char, int> ransomNoteStats, magazineStats;
    buildStats(ransomNote, ransomNoteStats);
    buildStats(magazine, magazineStats);
    for (const auto& pair : ransomNoteStats) {
        // if (magazineStats.find(pair.first) == magazineStats.end() ) {
        if (magazineStats.count(pair.first) == 0 ) {
            return false;
        } else {
            if (pair.second > magazineStats[pair.first] ) {
                return false;
            }
        }
    }
    return true;
}

int main() {
    string ransom = "aa", magazine = "aab";
    cout << canConstruct(ransom, magazine) << endl;
}