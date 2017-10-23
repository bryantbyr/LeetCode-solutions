//_553_Optimal_Division.java

//Created by bryantbyr on 20171023
//Time:O(n)
//Space:O(1)
//String
class Solution {
    public String optimalDivision(int[] nums) {
        if (nums.length == 1)
            return "" + nums[0];
        if (nums.length == 2)
            return nums[0] + "/" + nums[1];
        String res = "";
        for (int i = 0; i < nums.length ; ++i) {
            if (i == 0)
                res += nums[i] + "/(";
            else if (i == nums.length - 1)
                res += nums[i] + ")";
            else
                res += nums[i] + "/";
        }
        return res;
    }
}

//Learn from on discuss on 20171023
//Time:O(n)
//Space:O(1)
//String
class Solution {
    public String optimalDivision(int[] nums) {
        if (nums.length == 1)
            return String.valueOf(nums[0]);
        if (nums.length == 2)
            return nums[0] + "/" + nums[1];
        StringBuilder builder = new StringBuilder();
        for (int i = 0; i < nums.length ; ++i) {
            if (i == 0)
                builder.append(nums[i]).append("/(");
            else if (i != nums.length - 1)
                builder.append(nums[i] + "/");
            else
                builder.append(nums[i]).append(")");
        }
        return builder.toString();
    }
}

public class _553_Optimal_Division {
    public static void main(String[] args) {
        Solution S = new Solution();
        int[] nums = {1000, 100, 2, 10};
        System.out.println(S.optimalDivision(nums));
    }
}
