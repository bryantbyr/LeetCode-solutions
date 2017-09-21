//ContainsDuplicate.java
import java.util.Arrays;
import java.util.*;

//Created by bryantbyr on 20170921
//Time:O(nlog(n))
//Space:O(1)
//array
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        for (int i = 1; i < nums.length ; i++ ) {
            if (nums[i - 1] == nums[i])
                return true;
        }
        return false;
    }
}

//Learn from discuss on 20170921
//Time:O(n)
//Space:O(n)
//Hash Table
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i]))
                map.put(nums[i], map.get(nums[i]) + 1);
            else
                map.put(nums[i], 1);
            if(map.get(nums[i])>1)
                return true;
        }
        // for (Integer num : map.keySet()) {
        //     if (map.get(num) > 1) return true;
        // }
        return false;
    }
}
//Learn from discuss on 20170921
//Time:O(n)
//Space:O(n)
//set
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<Integer>();
        for (int i : nums) {
            // if (!set.add(i))
            //     return true;
            if (set.contains(i))
                return true;
            set.add(i);
        }
        return false;
    }
}

public class ContainsDuplicate {
    public static void main(String[] args) {
        int[] nums = {2, 5, 6, 1, 2, 9};
        Solution S = new Solution();
        System.out.println(S.containsDuplicate(nums));
    }
}
