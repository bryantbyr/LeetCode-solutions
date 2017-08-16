#include <iostream>
#include <vector>
using namespace std;

//20170809
//DP
class Solution {
public:
    int countSubstrings(string s) {
        int l=s.size();
        vector<vector<int>> dp(l,vector<int>(l,0));
        int r=0;
        for(int i=0;i<l;i++){
            dp[i][i]=1;
            for(int j=0;j<=i;j++){
                if(s[j]==s[i]&&(j+1>i-1||dp[j+1][i-1])){
                    dp[j][i]=1;
                    r++;
                }
            }
        }
        return r;
    }
};

int main()
{
    Solution s;
    cout<<s.countSubstrings("aaaaa")<<endl;
}
