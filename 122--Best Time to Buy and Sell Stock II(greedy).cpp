//122--Best Time to Buy and Sell Stock II(greedy).cpp

#include <iostream>
#include <vector>
using namespace std;

//20170327
//Time:O(N)
//Space:O(1)
//greedy
class Solution{
public:
    int maxProfit(vector<int>& prices)
    {
        int profit=0;
        for(int i=1;i<prices.size();i++){
            if(prices[i]-prices[i-1]>0)
                profit+=prices[i]-prices[i-1];
        }
        return profit;
    }
};

int main()
{
    Solution s;
    vector<int> v={2,1,2,3,6,4};

    cout<<s.maxProfit(v)<<endl;
    return 0;
}
