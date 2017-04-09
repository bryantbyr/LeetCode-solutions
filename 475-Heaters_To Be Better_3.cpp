//475-Heaters_To Be Better_3.cpp

//Author:@Bryant Byr 2017/03/14
//Time Complexity:O(NlogN)
//改进的快排+二分
//LeetCode AC

#include<iostream>
#include<vector>
using namespace std;

class Solution{
public:
    int findRadius(vector<int>& houses,vector<int>& heaters){
        QuickSort(heaters,0,heaters.size()-1);
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

    void QuickSort(vector<int>& s,int left,int right)
    {
        if(left>=right) return;
        int middle=(left+right)/2;
        int temp=s[left];
        if((s[middle]-s[left])*(s[middle]-s[right])<=0){
            s[left]=s[middle];
            s[middle]=temp;
            temp=s[left];
        }
        else if((s[right]-s[middle])*(s[right]-s[left])<=0){
            s[left]=s[right];
            s[right]=temp;
        }
        temp=s[left];
        int i=left;
        int j=right;
        int key=0;
        while(i!=j){
        if(key==0){
            while(s[j]>=temp){
                j--;
                if(j==i)
                    break;
            }
            if(i==j)
                break;
            s[i]=s[j];
            i++;

            key=1;
            }
            else{
                while(s[i]<=temp){
                    i++;
                    if(i==j)
                        break;
                }
                if(i==j)
                    break;
                s[j]=s[i];
                j--;

                key=0;
            }
        }
        s[i]=temp;
        QuickSort(s,left,i-1);
        QuickSort(s,i+1,right);
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


