//003-Longest Substring Without Repeated Characters.cpp

#include<iostream>
using namespace std;

//2017/03/19
//Time:O(n^4)
//Space:O(1)
//Brute Force(LeetCode Overtime)
class Solution{
public:
    int lengthOfLongestSubstring(string s)
    {
    	if(s.size()==0)
    		return  0;
        int Max=1;
        for(int i=0;i<s.size();i++){
            for(int j=i+1;j<s.size();j++){
                int key=0;
                int m=i;
                for(;m<j+1;m++){
                	int n=m+1;
                    for(;n<j+1;n++){
                        if(s[n]==s[m]){
                            key=1;
                            break;
                        }
                    }
                    if(key==1)
                        break;
                }
                if(key==1){
                    break;
                    key=0;
                }
                else
                    Max=max(Max,j-i+1);
            }
        }

        return Max;
    }
};


int main()
{
    Solution s;
    cout<<s.lengthOfLongestSubstring("pwwekw")<<endl;

    return 0;
}
