//003--Longest Substring Without Repeated Characters(Two Pointers).cpp

#include<iostream>
#include<vector>
using namespace std;

//2017/03/19
//Time:O(N)
//Space:O(N)
//A Better Two Pointers
class Solution{
public:
    int lengthOfLongestSubstring(string s)
    {
        if(s.size()==0)
            return  0;
        int i=0,j=0,maxLen=0;
        vector<int> pos(256,-1);
        for(;i<s.size();i++){
            if(pos[s[i]]>=j)
                j=pos[s[i]]+1;
            pos[s[i]]=i;
            maxLen=max(maxLen,i-j+1);
        }
        return maxLen;
    }
};


int main()
{
    Solution s;
    cout<<s.lengthOfLongestSubstring("")<<endl;

    return 0;
}
