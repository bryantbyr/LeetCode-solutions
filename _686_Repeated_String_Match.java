//_686_Repeated_String_Match.java

//Learn from discuss on 20171019
//Time:O(n)
//Space:O(1)
//String
class Solution {
    public int repeatedStringMatch(String A, String B) {
        int count = 0;
        StringBuilder s = new StringBuilder();
        while (s.length() < B.length()) {
            s.append(A);
            count++;
        }
        if (s.toString().contains(B))
            return count;
        if (s.append(A).toString().contains(B))
            return ++count;
        return -1;
    }
}

public class _686_Repeated_String_Match {
    public static void main(String[] args) {
        Solution S = new Solution();
        String A = "abcd", B = "cdabcdab";
        System.out.println(S.repeatedStringMatch(A, B));
    }
}
