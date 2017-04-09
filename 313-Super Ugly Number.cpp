//313-Super Ugly Number.cpp

#include<iostream>
#include<vector>
using namespace std;

class Solution{
    public:
        int nthSuperUglyNumber(int n,vector<int>& primes){
            int i=0;
            int* pos=new int[primes.size()];
            for(;i<primes.size();i++)
                pos[i]=0;
            int k=1;
            int* dp=new int[n];
            dp[0]=1;
            for(;k<n;k++){
                int min=dp[pos[0]]*primes[0];
                int s=1;
                for(;s<primes.size();s++)
                    if(min>dp[pos[s]]*primes[s])
                        min=dp[pos[s]]*primes[s];
                dp[k]=min;
                int m=0;
                for(;m<primes.size();m++){
                    if(dp[k]==dp[pos[m]]*primes[m])
                        pos[m]++;
                }
            }
            return dp[n-1];
        }
};

int main()
{
    Solution s;
    vector<int> v;
    v.push_back(2);
    v.push_back(7);
    v.push_back(13);
    v.push_back(19);
    cout<<s.nthSuperUglyNumber(12,v)<<endl;
    return 0;
}
