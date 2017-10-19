//_696_Count_Binary_Substrings.java

//Created by bryantbyr on 20171018
//Time:O(n)
//Space:O(1)
//String
// class Solution {
//     public int countBinarySubstrings(String s) {
//         int res = 0, cnt = 1, last = 1;
//         boolean flag = true, key = true;
//         for (int i = 0; i < s.length() - 1; ++i) {
//             if (flag && s.charAt(i + 1) == s.charAt(i)) {
//                 cnt++;
//                 last = cnt;
//             } else if (!flag && s.charAt(i + 1) == s.charAt(i)) {
//                 cnt--;
//             } else if (flag) {
//                 flag = false;
//             } else if (cnt > 1) {
//                 res += last - cnt + 1;
//                 i = i - last + cnt - 1;
//                 flag = true;
//                 key = false;
//             }
//             if (cnt == 1) {
//                 res += last;
//                 i = i - last + 1;
//                 flag = true;
//             }
//             if (!key && cnt > 1) {
//                 cnt = 1;
//                 last = 1;
//                 key = true;
//             }
//         }
//         if (!flag && cnt > 1)
//             res += last - cnt + 1;
//         return res;
//     }
// }

//Learn from discuss on 20171019
//Time:O(n)
//Space:O(1)
//String
class Solution {
    public int countBinarySubstrings(String s) {
        int res = 0, last = 0, cur = 1;
        for (int i = 1; i < s.length() ; ++i) {
            if (s.charAt(i) == s.charAt(i - 1))
                cur++;
            else {
                if (last != 0)
                    res += Math.min(last, cur);
                last = cur;
                cur = 1;
            }
        }
        if (last != 0)
            res += Math.min(last, cur);
        return res;
    }
}




//Learn from discuss on 20171019
//Time:O(n)
//Space:O(1)
//String (smart)
class Solution {
    public int countBinarySubstrings(String s) {
        int prevRunLength = 0, curRunLength = 1, res = 0;
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == s.charAt(i - 1))
                curRunLength++;
            else {
                prevRunLength = curRunLength;
                curRunLength = 1;
            }
            if (prevRunLength >= curRunLength)
                res++;
        }
        return res;
    }
}

public class _696_Count_Binary_Substrings {
    public static void main(String[] args) {
        Solution S = new Solution();
        System.out.println(S.countBinarySubstrings("000100"));
    }
}
