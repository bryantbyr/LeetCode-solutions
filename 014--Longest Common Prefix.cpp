#include<iostream>
#include<vector>
using namespace std;


class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.size()==0)return "";
        return dcHelper(strs,0,strs.size()-1);
    }
    string dcHelper(vector<string>& strs,int low,int high)
    {
        if(low==high)return strs[low];
        int mid=low+(high-low)/2;
        string str1=dcHelper(strs,low,mid);
        string str2=dcHelper(strs,mid+1,high);
        return Common(str1,str2);
    }

    string Common(string str1,string str2)
    {
        unsigned int i=0;
        for(;str1[i]==str2[i]&&i<str1.length()&&i<str2.length();i++);
            return str1.substr(0,i);
    }

};

int main()
{
	Solution s;
	//string str[] = { "", "", "" };
	//vector<string> strs(str, str + 3);

	vector<string> strs ;
	//strs.resize(3);
	strs = { "", "", "" };
	s.longestCommonPrefix(strs);
	return 0;
}
