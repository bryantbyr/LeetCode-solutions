//240-Search a 2D Matrix II.cpp
//20170316
#include<iostream>
#include<vector>
using namespace std;

//Author:bryantbyr
//Time Complexity:O(logM)~O(NlogM)
//Space Complexity:O(1)
//思路:先用一次二分法确定target可能在的行的范围，
       //然后在该范围内分别对每行用二分法进行查找
class Solution{
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target)
    {
        if(matrix.size()==0||matrix[0].size()==0)
            return false;
        int start=0;
        int end=matrix.size()-1;
        while(start<=end){//确定target可能在的行的范围:0~end
            int middle=start+(end-start)/2;
            if(matrix[middle][0]==target)return true;
            if(matrix[middle][0]>target)
                end=middle-1;
            else
                start=middle+1;
        }
        if(end<0)return false;

        for(int i=0;i<=end;i++){//在可能存在的范围内对每行用进行查找
            int start=0;
            int end=matrix[i].size()-1;
            while(start<=end){
                int middle=start+(end-start)/2;
                if(matrix[i][middle]==target)return true;
                if(matrix[i][middle]>target)
                    end=middle-1;
                else
                    start=middle+1;
            }
        }
        return false;
    }
};

int main()
{
    Solution s;
    vector<std::vector<int>> m;
    m={{1,4,7,11,15},{2,5,8,12,19},{3,6,9,16,22},{10,13,14,17,24},
    {10,13,14,17,24},{18,21,23,26,30}};
    cout<<s.searchMatrix(m,5)<<endl;

    return 0;
}
