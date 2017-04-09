//Ugly Number II-version 3.cpp

#include<iostream>
using namespace std;

class Solution{
    public:
		inline int Min(int a,int b,int c)
		{
			if(a<=b&&a<=c)
				return a;
			else if(b<=a&&b<=c)
				return b;
			else if(c<=a&&c<=b)
				return c;
		}
        int nthUglyNumber(int n){
			int i1=0;int i2=0;int i3=0;
			int* dp=new int[n];
			dp[0]=1;
            int k=1;
			for(;k<n;k++)
			{
				dp[k]=Min(dp[i1]*2,dp[i2]*3,dp[i3]*5);
				if(dp[k]==dp[i1]*2)
					i1++;
				if(dp[k]==dp[i2]*3)
					i2++;
				if(dp[k]==dp[i3]*5)
					i3++;
			}
			return dp[n-1];
        }
};

int main()
{
    Solution s;
    cout<<s.nthUglyNumber(1660)<<endl;
    return 0;
}
