//122-Best Time to Sell Stock II(dp).cpp

#include <iostream>
#include <vector>
using namespace std;

//20170327
//Time:O(N)
//Space:O(1)
//dp
class Solution{
public:
    int maxProfit(vector<int>& prices)
    {
    	if(prices.size()==0)
    		return 0;
        int* dp=new int[prices.size()];
        dp[0]=0;
        int i=1;
        for(;i<prices.size();i++){
            if(prices[i]-prices[i-1]>0)
                dp[i]=dp[i-1]+prices[i]-prices[i-1];
            else
                dp[i]=dp[i-1];
        }
        return dp[i-1];
    }
};

int main()
{
    Solution s;
    vector<int> v={2,1,2,3,6,4};

    cout<<s.maxProfit(v)<<endl;
    return 0;
}
