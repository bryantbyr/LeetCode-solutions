//278-First Bad Version.cpp

#include<iostraem>
#include<vector>
using namespace std;

bool isBadVersion(int version);

//Author:bryantbyr
//Time Complexity:O(logN)
//Space Complexity:O(1)
//算法思想:二分法
class Solution{
    public:
        int firstBadVersion(int n)
        {
            int start=1;
            int end=n;
            while(start<=end){
                int middle=start+(end-start)/2;
                if(isBadVersion(middle))
                    end=middle-1;
                else
                    start=middle+1;
            }
            return end+1;
        }
};

int main()
{


    return 0;
}
