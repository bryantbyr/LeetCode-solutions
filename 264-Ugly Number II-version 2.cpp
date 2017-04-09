//Ugly Number II-version 2.cpp

#include<iostream>
using namespace std;

class Solution{
    public:
        int nthUglyNumber(int n){
            unsigned long long* dp=new unsigned long long[n];
            dp[0]=1;
            dp[1]=2;
            int i=2;
            for(;i<n;i++)
            {
                int min=INT_MAX;
                int k=0;
                int key=0;
                for(;k<i-1;k++)
                {
                    if(dp[k]*2>dp[i-1]&&dp[k]*2<min)
                    {
                        min=dp[k]*2;
						key++;
						if(key==4)
						{
							key=0;
                    		break;
						}	
					}
                    else if((dp[k]*3)>dp[i-1]&&(dp[k]*3)<min)
                    {
						min=dp[k]*3;
						key++;
						if(key==4)
						{
							key=0;
                    		break;
						}
					}
                    else if((dp[k]*5)>dp[i-1]&&(dp[k]*5)<min)
                    {
						min=(dp[k]*5);
						key++;
						if(key==4)
						{
							key=0;
                    		break;
						}
					}
                }
                dp[i]=min;
            }
            return dp[n-1];
        }
};

int main()
{
    Solution s;
    cout<<s.nthUglyNumber(1690)<<endl;
    return 0;
}
