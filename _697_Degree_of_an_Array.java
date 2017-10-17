//_697_Degree_of_an_Array.java

import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.Map.Entry;

//Created by bryantbyr on 20171016
//Time:O(nlog(n))
//Space:O(n)
//Array + String
class Solution {
    public int findShortestSubArray(int[] nums) {
        int[] sortedNums;
        sortedNums = (int[])nums.clone();
        // int[] sortedNums = new int[nums.length];
        // System.arraycopy(sortedNums, 0, nums, 0, nums.length);

        Arrays.sort(sortedNums);
        List<Integer> list = new ArrayList<>();
        int degree = 0, temp = 1;
        for (int i = 1; i < sortedNums.length; ++i) {
            if (sortedNums[i] == sortedNums[i - 1])
                temp++;
            else {
                if (temp > degree) {
                    list.clear();
                    list.add(sortedNums[i - 1]);
                    degree = temp;
                } else if (temp == degree)
                    list.add(sortedNums[i - 1]);
                temp = 1;
            }
        }
        if (temp > degree) {
            list.clear();
            list.add(sortedNums[sortedNums.length - 1]);
        } else if (temp == degree)
            list.add(sortedNums[sortedNums.length - 1]);

        String s = new String(nums, 0, nums.length);
        int res = Integer.MAX_VALUE;
        for (int i = 0; i < list.size(); ++i)
            res = Math.min(res, s.lastIndexOf(list.get(i)) - s.indexOf(list.get(i)) + 1);

        return res == Integer.MAX_VALUE ? 1 : res;
    }
}

//Created by bryantbyr on 20171016
//Time:O(nlog(n))
//Space:O(n)
//Array + String
class Solution {
    public int findShortestSubArray(int[] nums) {
        String s = new String(nums, 0, nums.length);
        Arrays.sort(nums);
        List<Integer> list = new ArrayList<>();
        int degree = 0, temp = 1;
        for (int i = 1; i < nums.length; ++i) {
            if (nums[i] == nums[i - 1])
                temp++;
            else {
                if (temp > degree) {
                    list.clear();
                    list.add(nums[i - 1]);
                    degree = temp;
                } else if (temp == degree)
                    list.add(nums[i - 1]);
                temp = 1;
            }
        }
        if (temp > degree) {
            list.clear();
            list.add(nums[nums.length - 1]);
        } else if (temp == degree)
            list.add(nums[nums.length - 1]);
        int res = Integer.MAX_VALUE;
        for (int i = 0; i < list.size(); ++i)
            res = Math.min(res, s.lastIndexOf(list.get(i)) - s.indexOf(list.get(i)) + 1);
        return res == Integer.MAX_VALUE ? 1 : res;
    }
}

//Created by bryantbyr on 20171016
//Time:O(n)
//Space:O(n)
//Array + Hash Table
class Solution {
    public int findShortestSubArray(int[] nums) {
        Map<Integer, Integer> map1 = new HashMap<>();
        Map<Integer, Integer[]> map2 = new HashMap<>();
        int degree = 0;
        for (int i = 0; i < nums.length; ++i) {
            map1.put(nums[i], map1.getOrDefault(nums[i], 0) + 1);
            degree = Math.max(map1.get(nums[i]), degree);
            if (!map2.containsKey(nums[i])) {
                Integer[] range = new Integer[2];
                range[0] = i;
                map2.put(nums[i], range);
            }
            map2.get(nums[i])[1] = i;
        }
        int res = nums.length;
        for (Map.Entry<Integer, Integer[]> entry : map2.entrySet()) {
            if (map1.get(entry.getKey()) == degree)
                res = Math.min(res, entry.getValue()[1] - entry.getValue()[0] + 1);
        }
        return res;

    }
}

public class _697_Degree_of_an_Array {
    public static void main(String[] args) {
        Solution S = new Solution();
        int[] nums = {1, 2, 2, 3, 1, 4, 2};
        System.out.println(S.findShortestSubArray(nums));
    }
}
