//524-Longest Word in Dictionary through Deleting.cpp

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

//20170407
//Time:O(NlogN)
//Space:O(1)
//排序，然后从头遍历寻找第一个符合要求的字符串
bool sortByLength(const string& s1,const string& s2)
{
    if(s1.size()>s2.size())
        return true;
    else if(s1.size()==s2.size())
        return s1.compare(s2)<0;
    else
        return false;
}

class Solution {
public:
    string findLongestWord(string s, vector<string>& d) {
        sort(d.begin(),d.end(),sortByLength);
        for(int i=0;i<d.size();i++){
            int pos=0;
            for(int k=0;k<s.size()&&pos<d[i].size();k++){
                if(s[k]==d[i][pos])
                    pos++;
            }
            if(pos==d[i].size())
            	return d[i];
        }
        return "";
    }
};

int main()
{
    Solution S;
    vector<string> d={"a","b","c"};
    string s="abpcplea";
    string r=S.findLongestWord(s,d);
    cout<<r<<endl;
    return 0;
}
