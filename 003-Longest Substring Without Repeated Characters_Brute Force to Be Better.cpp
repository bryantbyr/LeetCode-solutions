//003-Longest Substring Without Repeated Characters.cpp

#include<iostream>
#include<vector>
using namespace std;

//2017/03/19
//Time:O(n^3)
//Space:O(n)
//Brute Force
class Solution{
public:
    int lengthOfLongestSubstring(string s)
    {
        if(s.size()==0)
            return  0;

        int  maxLen=0;
        vector<int> pos(256,s.size());
        for(int i=0;i<s.size();i++){
        	pos.clear();
        	for(int m=0;m<256;m++)
        		pos.push_back(s.size()); 
            for(int j=i;j<s.size();j++){
            	int k=i;
                for(;k<j+1;k++){
                    if(pos[s[k]]<k)
                        break;
                    pos[s[k]]=k;
                }
                maxLen=max(maxLen,k-i);
                if(pos[s[k]]<k)
                   break;
            }
        }
        return maxLen;
    }
};


int main()
{
    Solution s;
    cout<<s.lengthOfLongestSubstring("pwwekw")<<endl;

    return 0;
}
