#include<iostream>
#include<string>
#include<sstream>
using namespace std;

class Solution
{
public:
    int calculate(string s)
    {
        istringstream iss('+' + s + '+');
        char op;
        int res = 0;
        int cur = 0;
        while (iss >> op)
        {
            if (op == '+' || op == '-')
            {
                res += cur;
                iss >> cur;
                if (op == '-')
                    cur = -cur;
            }
            else
            {
                int n;
                iss >> n;
                if (op == '*')
                    cur *= n;
                else
                    cur /= n;
            }
        }
        return res;
    }
};

int main()
{
    Solution s;
    cout << s.calculate("9+6/2") << endl;
    return 0;
}
