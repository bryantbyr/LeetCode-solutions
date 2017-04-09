//475-Heaters.cpp

//@Author:bryantbyr 2017/03/13
//Time Complexity:O(N^2)
//思路:暴力法
//LeetCode OverTime

#include<iostream>
#include<vector>
#include<math.h>
#include<limits.h>
using namespace std;

class Solution{
public:
    int findRadius(vector<int>& houses,vector<int>& heaters){
        int* h=new int[houses.size()];
        int k=0;
        for(;k<houses.size();k++){
            h[k]=INT_MAX;
        }
        int res=0;
        int i=0;
        for(;i<houses.size();i++){
            int j=0;
            for(;j<heaters.size();j++){
                if(abs(houses[i]-heaters[j])<h[i])
                    h[i]=abs(houses[i]-heaters[j]);
            }
            if(res<h[i])
                res=h[i];
        }
        return res;
    }
};

int main()
{
    Solution s;
    vector<int> houses;
    vector<int> heaters;
//    houses={1,2,3,4,5,6,7,8};
//    heaters={1,7};

	for(int i=1;i<22227;i++)
	    houses.push_back(i);
	for(int i=2;i<22227;i++)
	    heaters.push_back(i);
    cout<<s.findRadius(houses,heaters)<<endl;

    return 0;
}
