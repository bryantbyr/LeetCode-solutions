//MaximumProductOfThreeNumbers.java
import java.util.*;
import java.lang.*;

//Created by bryantbyr on 20170922
//Time:O(nlog(n))
//Space:O(1)
//array
class Solution {
    public int maximumProduct(int[] nums) {
        Arrays.sort(nums);
        int t1 = nums[nums.length - 1] * nums[nums.length - 2] * nums[nums.length - 3];
        int t2 = nums[0] * nums[1] * nums[nums.length - 1];
        return Math.max(t1, t2);
    }
}

public class MaximumProductOfThreeNumbers {
    public static void main(String[] args) {
        int[] nums = {1, 3, 2, 4};
        Solution S = new Solution();
        System.out.println(S.maximumProduct(nums));
    }
}
