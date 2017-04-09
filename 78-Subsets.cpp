//78-Subsets.cpp

#include<iostream>
#include<vector>
using namespace std;

//2017/03/22
//Time:O(2^N)
//Space:O(1)
//遍历+迭代
class Soluiton{
public:
    vector<vector<int>> subsets(vector<int>& nums)
    {
        vector<vector<int>> r={{}};
        for(int k=0;k<nums.size();k++){
        	int end=r.size();
            for(int i=0;i<end;i++){
            	vector<int> t=r[i];
            	t.push_back(nums[k]);
                r.push_back(t);
            }
        }

        return r;
    }

};

int main()
{
    Soluiton s;
    vector<int> v={1,2,5,3,6};
    vector<vector<int>> r=s.subsets(v);

    for(int k=0;k<r.size();k++){
        for(int j=0;j<r[k].size();j++)
            cout<<r[k][j]<<" ";
        cout<<endl;
    }

    return 0;
}
