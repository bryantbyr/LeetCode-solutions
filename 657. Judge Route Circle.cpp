//657. Judge Route Circle.cpp
#include <iostream>
using namespace std;

//Created by bryantbyr
//Time:O(n)
//Space:O(1)
//string
class Solution {
public:
    bool judgeCircle(string moves) {
        int l = 0, r = 0, u = 0, d = 0;
        for (unsigned i = 0; i < moves.size(); i++) {
            if (moves[i] == 'L')
                l++;
            else if (moves[i] == 'R')
                r++;
            else if (moves[i] == 'U')
                u++;
            else
                d++;
        }
        return l == r && u == d;
    }
};

int main()
{
    Solution S;
    string s = "LRUD";
    cout << S.judgeCircle(s) << endl;
}
