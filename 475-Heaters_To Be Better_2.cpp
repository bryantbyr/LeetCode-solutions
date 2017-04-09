//475-Heaters_To Be Better_2.cpp

//@Author:bryantbyr 2017/03/14
//TimeComplexity:O(NlogN)
//思路：合并排序+二分法
//LeetCode AC

#include<iostream>
#include<vector>
using namespace std;

class Solution{
public:
    int findRadius(vector<int>& houses,vector<int>& heaters){
        MergeSort(heaters,0,heaters.size()-1);
        int* h=new int[houses.size()];
        int res=0;
        int key=0;
        for(int i=0;i<houses.size();i++){
            int left=0;
            int right=heaters.size()-1;
            int middle=(right+left)/2;
            key=0;
            if(houses[i]<=heaters[left]){
                h[i]=abs(houses[i]-heaters[left]);
                key=1;
            }
            if(houses[i]>=heaters[right]){
                h[i]=abs(houses[i]-heaters[right]);
                key=1;
            }
            while(right-left>=1){
                middle=(right+left)/2;
                if(heaters[middle]==houses[i]){
                    h[i]=0;
                    break;
                }
                else if(heaters[middle]<houses[i])
                    left=middle+1;
                else
                    right=middle-1;
            }
            if(key==0){
                if(heaters[middle]==houses[i])
                    h[i]=0;
                else{
                    if((heaters.size()-1)<(left+1))
                        h[i]=abs(houses[i]-heaters[left])>=abs(houses[i]-heaters[left-1])?
                                 abs(houses[i]-heaters[left-1]):abs(houses[i]-heaters[left]);
                    else if((left-1)==-1)
                            h[i]=abs(houses[i]-heaters[left])>=abs(houses[i]-heaters[left+1])?
                                 abs(houses[i]-heaters[left+1]):abs(houses[i]-heaters[left]);
                    else
                        h[i]=Min(abs(houses[i]-heaters[left]),abs(houses[i]-heaters[left-1]),
                                 abs(houses[i]-heaters[left+1]));
                }
            }
            if(res<h[i])
                res=h[i];
        }
        return res;
    }

    inline int Min(int a,int b,int c)
    {
        if(a<=b&&a<=c)
            return a;
        else if(b<=a&&b<=c)
            return b;
        else
            return c;
    }

    void Merge(vector<int>& s,int l,int r)
    {
        int i=l;
        int j=l+(r-l)/2+1;
        int countI=l+(r-l)/2;
        while(i<=countI&&j<=r){
            if(s[j]<s[i]){
                int temp=s[j];
                int k=j-1;
                while(k>=i){
                    s[k+1]=s[k];
                    k--;
                }
                countI++;
                s[i]=temp;
                j++;
            }
            i++;
        }
    }

    void MergeSort(vector<int>& s,int left,int right)
    {
        if(left==right)
            return;
        MergeSort(s,left,left+(right-left)/2);
        MergeSort(s,left+(right-left)/2+1,right);
        Merge(s,left,right);
        return;
    }
};

int main()
{
    Solution s;
    vector<int> houses;
    vector<int> heaters;
    // houses={1,2,3,4,7};
    // heaters={1,4};

    for(int i=1;i<22227;i++)
        houses.push_back(i);
    for(int i=2;i<22227;i++)
        heaters.push_back(i);
    cout<<s.findRadius(houses,heaters)<<endl;

    return 0;
}

