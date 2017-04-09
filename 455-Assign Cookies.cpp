//455-Assign Cookies.cpp

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

//20170329
//Time:O(NlogN)
//Space:O(N)
//排序之后对两个数组进行比较
class Solution{
public:
    int findContentChildren(vector<int>& g, vector<int>& s)
    {
        sort(g.begin(),g.end());
        sort(s.begin(),s.end());
        int i=0,j=0,count=0;
        while(i<g.size()&&j<s.size()){
            if(g[i]<=s[j]){
                i++;
                count++;
            }
            j++;
        }
        return count;
    }
};

int main()
{
    Solution s;
    vector<int> g={1,2,3};
    vector<int> ss={1,1};
    cout<<s.findContentChildren(g,ss)<<endl;

    return 0;
}
