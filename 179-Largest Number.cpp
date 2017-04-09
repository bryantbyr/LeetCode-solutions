//179-Largest Number.cpp

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

//20170406
//Time:O(NlogN)
//Space:O(logN)
//自定义c++_sort函数的形式参数cmp(),以对原数组实现合理的排序,然后将其首尾相连拼接成字符串
int getIntegerLength(int num)
{
    if(num==0)
        return 1;
    int length=0;
    while(num!=0){
        length++;
        num/=10;
    }
    return length;
}
bool SortByFirstInteger(const int& a,const int& b)
{
	int t1 = (getIntegerLength(a) - 1),t2 = (getIntegerLength(b) - 1);
	int temp1 = a, temp2 = b;
	while (t1 >= 0 || t2 >= 0){
		while (t1 >= 0){
			temp2 = b;
			t2 = (getIntegerLength(temp2) - 1);
			while (t1 >= 0 && t2 >= 0){
				if (temp1 / (int)pow(10, t1) > temp2 / (int)pow(10, t2))
					return true;
				else if (temp1 / (int)pow(10, t1) == temp2 / (int)pow(10, t2)){
					temp1 = temp1 % (int)pow(10, t1);
					temp2 = temp2 % (int)pow(10, t2);
				}
				else
					return false;
				t1--;
				t2--;
			}
		}
		while (t2 >= 0){
			temp1 = a;
			t1 = (getIntegerLength(temp1) - 1);
			while (t2 >= 0 && t1 >= 0){
				if (temp2 / (int)pow(10, t2) > temp1 / (int)pow(10, t1))
					return false;
				else if (temp2 / (int)pow(10, t2) == temp1 / (int)pow(10, t1)){
					temp2 = temp2 % (int)pow(10, t2);
					temp1 = temp1 % (int)pow(10, t1);
				}
				else
					return true;
				t2--;
				t1--;
			}
		}
	}
	return false;
}

class Solution {
public:
    string largestNumber(vector<int>& nums){
        string s="";
        sort(nums.begin(),nums.end(),SortByFirstInteger);
        for(int i=0;i<nums.size();i++){
            int t=getIntegerLength(nums[i])-1;
            while(t>=0){
                s.push_back(nums[i]/(int)pow(10,t)+'0');
                nums[i]=nums[i]%(int)pow(10,t);
                t--;
            }
        }
		if (s[0] == '0')
			return "0";
        return s;
    }
};

int main()
{
    Solution s;
	vector<int> v = {121,12,9,23};
    string ss=s.largestNumber(v);
    cout<<ss<<endl;
    return 0;
}
