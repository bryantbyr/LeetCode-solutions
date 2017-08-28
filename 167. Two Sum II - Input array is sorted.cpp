//167. Two Sum II - Input array is sorted.cpp
#include <iostream>
#include <vector>
using namespace std;

//Created by bryantbyr on 20170828
//Time:O(n^2)
//Space:O(n)
//Two Pointers
// class Solution {
// public:
//     vector<int> twoSum(vector<int>& numbers, int target) {
//         vector<int> r = {};
//         for (unsigned i = 0; i < numbers.size(); ++i) {
//             for (unsigned j = i + 1; j < numbers.size(); ++j) {
//                 if (numbers[i] + numbers[j] == target) {
//                     r.push_back(i + 1);
//                     r.push_back(j + 1);
//                     return r;
//                 }
//                 else if (numbers[i] + numbers[j] > target)
//                     break;
//             }
//         }
//         return r;
//     }
// };

//Learn from discuss on 20170828
//Time:O(n)
//Space:O(n)
//Binary Search / Two Pointers
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> r = {};
        int start = 0, end = numbers.size() - 1;
        while (start < end) {
            if (numbers[start] + numbers[end] > target)
                end--;
            else if (numbers[start] + numbers[end] < target)
                start ++;
            else {
                r.push_back(start + 1);
                r.push_back(end + 1);
                break;
            }
        }
        return r;
    }
};


int main()
{
    Solution s;
    vector<int> numbers = {2, 7, 11, 15};
    int target = 9;
    vector<int> r = s.twoSum(numbers, target);
    for (unsigned int i = 0; i < r.size(); ++i) {
        cout << r[i] << endl;
    }
}
