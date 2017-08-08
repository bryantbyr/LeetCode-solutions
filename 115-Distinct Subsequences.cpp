#include <iostream>
#include <vector>
using namespace std;


class Solution {
public:
    int numDistinct(string s, string t) {
        int m=s.size();
        int n=t.size();
        vector<vector<int> > dp(m+1,vector<int>(n+1));
        for(int i=0;i<=m;i++)
            dp[i][0]=1;
        for(int i=0;i<=m;i++){
            for(int j=i+1; j <= n;j++)
                dp[i][j]=0;
        }
        for(int i=1;i<=m;i++)
            for(int j=1;j<=i&&j<=n;j++){
                if(s[m-i]==t[n-j])
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j];
                else
                    dp[i][j]=dp[i-1][j];
            }
        return dp[m][n];
    }
};

int main()
{
    Solution S;
    string t="ABCDE";
    string s="ACE";
    cout<<S.numDistinct(t,s)<<endl;
}
