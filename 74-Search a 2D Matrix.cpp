//74-Search a 2D Matrix.cpp

#include<iostream>
#include<vector>
using namespace std;

//Author:bryantbyr
//Time Complexity:O(logN)
//Space Complexity:O(1)
//两次运用二分法
class Solution{
public:
    bool searchMatrix(vector<vector<int>>& matrix,int target){
        if(matrix.size()==0)//判断矩阵是否为空
            return false;
        else if(matrix[0].size()==0)
            return false;

        int start1=0;
        int end1=matrix.size()-1;
        while(start1<=end1){//第一次运用二分法，确定元素所在行
            int middle1=start1+(end1-start1)/2;
            if(matrix[middle1][0]==target)
                return true;
            if(matrix[middle1][0]>target)
                end1=middle1-1;
            else
                start1=middle1+1;
        }
        if(end1<0)//如果在第一行之前，即不存在
            return false;

        int start2=0;
        int end2=matrix[end1].size()-1;
        while(start2<=end2){//第二次运用二分法，在该行中查找元素
            int middle2=start2+(end2-start2)/2;
            if(matrix[end1][middle2]==target)
                return true;
            if(matrix[end1][middle2]>target)
                end2=middle2-1;
            else
                start2=middle2+1;
        }
        return false;
    }
};


int main()
{
    Solution s;
    vector<vector<int>> m;
    m={{1,1}};

    //m={{2,3,5,7},{10,11,16,20},{23,30,34,50}};

    cout<<s.searchMatrix(m,0)<<endl;

    return 0;
}
