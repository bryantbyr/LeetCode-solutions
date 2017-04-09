#include<iostream>
#include<vector>
using namespace std;

class Solution{
    public:
        int maxProfit(vector<int>& prices){
            if(prices.size()==NULL||prices.size()<=1)
                return 0;
			int* dp=new int[prices.size()];
			int* min=new int[prices.size()];
			min[0]=prices[0];
			dp[0]=0;
            int i=1;
            int max=0;
            for(;i<prices.size();i++)
            {
				min[i]=(min[i-1]<prices[i-1]?min[i-1]:prices[i-1]);
				dp[i]=(dp[i-1]>(prices[i]-min[i])?dp[i-1]:(prices[i]-min[i]));
            }
            return dp[prices.size()-1];
        }
};

int main()
{
    Solution s;
    vector<int> prices;
    prices={2,1,4};
	cout << s.maxProfit(prices) << endl;;
	//system("pause");
    return 0;
}
