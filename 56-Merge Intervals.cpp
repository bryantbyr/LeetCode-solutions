//56-Merge Intervals.cpp

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

//20170405
//Time:O(NlogN)
//Space:O(1)
//排序+一次遍历
struct Interval{
    int start;
    int end;
    Interval() : start(0), end(0) {}
    Interval(int s, int e) : start(s), end(e) {}
};

bool SortByStart(Interval i1,Interval i2)
{
    return i1.start<i2.start;
}

class Solution {
public:
    vector<Interval> merge(vector<Interval>& intervals) {
        if(intervals.size()==0)
            return {};
        vector<Interval> r;
        sort(intervals.begin(),intervals.end(),SortByStart);
        int i=1;
        for(;i<intervals.size();i++){
            if(intervals[i].start<=intervals[i-1].end){
                intervals[i].start=intervals[i-1].start;
                if(intervals[i].end>intervals[i-1].end)
                    intervals[i].end=intervals[i-1].end;
            }
            else
                r.push_back(intervals[i-1]);
        }
        r.push_back(intervals[i-1]);
        return r;
    }
};

int main()
{
    Solution s;
    vector<Interval> i;
    i.push_back(Interval(1,3));
    i.push_back(Interval(2,6));
    i.push_back(Interval(8,10));
    i.push_back(Interval(15,18));

    vector<Interval> r=s.merge(i);
    for(int i=0;i<r.size();i++){
        cout<<r[i].start<<" "<<r[i].end<<endl;
    }

    return 0;
}
