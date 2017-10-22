//_521_Longest_Uncommon_Subsequence_I.java

//Learn from discuss on 20171022
//Time:O(n)
//Space:O(1)
//String
class Solution {
    public int findLUSlength(String a, String b) {
        if (a.equals(b))
            return -1;
        return Math.max(a.length(), b.length());
    }
}

public class _521_Longest_Uncommon_Subsequence_I {
    public static void main(String[] args) {
        Solution S = new Solution();
        String s1 = "abd", s2 = "acd";
        System.out.println(S.findLUSlength(s1, s2));
    }
}
