#include<iostream>
#include<vector>
using namespace std;

class Solution{
public:
    vector<int> twoSum(vector<int>& nums,int target)
    {
        vector<int> s;
		int k = 0;
        for (int i = 0; i < nums.size(); ++i)
        {
            for (int j = i+1; j < nums.size(); ++i)
            {
                if((nums[i]+nums[j])==target)
                {
					s.push_back(i);
					s.push_back(j);
					k = 1;
					break;
                }
            }
			if (k == 1)
				break;
        }
		return s;
    }
};

int main()
{


	return 0;
}
