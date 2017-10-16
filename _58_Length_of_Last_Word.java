//_58_Length_of_Last_Word.java

//Created by bryantbyr on 20171016
//Time:O(n)
//Space:O(n)
//String + Stack
class Solution {
    public int lengthOfLastWord(String s) {
        int res = 0;
        for (int i = s.length() - 1; i >= 0; --i) {
            if (s.charAt(i) != ' ')
                res++;
            else if (res != 0)
                // return res;
                break;
        }
        return res;
    }
}

//Created by bryantbyr on 20171016
//Time:O(n)
//Space:O(n)
//String + Stack
class Solution {
    public int lengthOfLastWord(String s) {
        int res = 0;
        s = s.trim();
        for (int i = s.length() - 1; i >= 0; --i) {
            if (s.charAt(i) != ' ')
                res++;
            else
                break;
        }
        return res;
    }
}

//Created by bryantbyr on 20171016
//Time:O(n)
//Space:O(n)
//String + Stack
class Solution {
    public int lengthOfLastWord(String s) {
        s = s.trim();
        if (s.length() == 0)
            return 0;
        String[] t = s.split(" ");
        return t[t.length - 1].length();
    }
}

//Learn from discuss on 20171016
//Time:O(n)
//Space:O(n)
//String + Stack
class Solution {
    public int lengthOfLastWord(String s) {
        return s.trim().length() - s.trim().lastIndexOf(" ") - 1;
        // s = s.trim();
        // int lastIndex = s.lastIndexOf(' ') + 1;
        // return s.length() - lastIndex;
    }
}

public class _58_Length_of_Last_Word {
    public static void main(String[] args) {
        Solution S = new Solution();
        System.out.println(S.lengthOfLastWord("Hello"));
    }
}
