//003-Longest Substring Without Repeated Characters(Two Pointers).cpp

#include<iostream>
using namespace std;

//2017/03/19
//Time:O(N^2)
//Space:O(1)
//Two Pointers
class Solution{
public:
    int lengthOfLongestSubstring(string s)
    {
        if(s.size()==0)
            return  0;
        int i=0,j=0;
        int count=0,maxLen=0;
        for(;i<s.size();i++){
            for(int k=j;k<=i-1;k++){
                if(s[k]==s[i]){
                    j=k+1;
                    break;
                }
            }
            maxLen=max(maxLen,i-j+1);
        }
        return maxLen;
    }
};


int main()
{
    Solution s;
    cout<<s.lengthOfLongestSubstring("ccccc")<<endl;

    return 0;
}
