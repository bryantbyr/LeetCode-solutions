//ContainsDuplicateII_219.java
import java.util.*;

//Created by bryantbyr on 20170923
//Time:O(n)
//Space:O(n)
//array + HashMap
class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length ; ++i ) {
            if (map.containsKey(nums[i]) && i - map.get(nums[i]) <= k)
                return true;
            map.put(nums[i], i);
        }
        return false;
    }
}

//Created by bryantbyr on 20170923
//Time:O(n)
//Space:O(n)
//array + HashMap
class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < nums.length ; ++i ) {
            if (i > k)
                set.remove(nums[i - k - 1]);
            if (set.contains(nums[i]))
                return true;
            set.add(nums[i]);
        }
        return false;
    }
}

public class ContainsDuplicateII_219 {
    public static void main(String[] args) {
        int[] nums = {2, 1, 6, 3, 4, 2, 7, 4};
        Solution S = new Solution();
        System.out.println(S.containsNearbyDuplicate(nums, 4));
    }
}
