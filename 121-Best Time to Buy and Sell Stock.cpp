//Best Time to Buy and Sell Stock.cpp

#include<iostream>
#include<vector>
using namespace std;

class Solution{
    public:
        int maxProfit(vector<int>& prices){
            if(prices.size()==NULL||prices.size()<=1)
                return 0;
            int k=1;
            int i=0;
            int max=0;
            for(;k<prices.size();k++)
            {
				i = 0;
                for(;i<k;i++)
                {
                    if((prices[k]-prices[i])>max)
                        max=prices[k]-prices[i];
                }
            }
            return max;
        }
};

int main()
{
    Solution s;
    vector<int> prices;
    prices={7,1,5,3,6,4};
	cout << s.maxProfit(prices) << endl;;
	//system("pause");
    return 0;
}
