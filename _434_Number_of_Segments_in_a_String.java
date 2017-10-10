//_434_Number_of_Segments_in_a_String.java

//Created by bryantbyr on 20171010
//Time:O(n)
//Space:O(1)
//String
class Solution {
    public int countSegments(String s) {
        int res = 0;
        for (int i = 0; i < s.length(); ++i) {
            // if ((i == 0 && s.charAt(i) != ' ') || (s.charAt(i) != ' ' && s.charAt(i - 1) == ' '))
            if (s.charAt(i) != ' ' && (i == 0 || s.charAt(i - 1) == ' '))
                res++;
        }
        return res;
    }
}

//Created by bryantbyr on 20171010
//Time:O(n)
//Space:O(1)
//String
class Solution {
    public int countSegments(String s) {
        if (s.length() == 0)
            return 0;
        int res = 0;
        for (int i = 0; i < s.length(); ++i) {
            boolean flag = false;
            while (i < s.length() && s.charAt(i) == ' ') {
                flag = true;
                i++;
            }
            if (flag && i != s.length())
                res++;
        }
        return s.charAt(0) == ' ' ? res : res + 1;
    }
}

//Learn from discuss on 20171010
//Time:O(n)
//Space:O(1)
//String
class Solution {
    public int countSegments(String s) {
        int result = 0, n = s.length();
        char[] arr = s.toCharArray();//常用的String处理方式
        for (int i = 0; i < n; i++) {
            if (arr[i] == ' ')
                continue;
            result++;
            while (i < n && arr[i] != ' ')
                i++;
        }
        return result;
    }
}

//Learn from discuss on 20171010
//Time:O(n)
//Space:O(1)
//String
class Solution {
    public int countSegments(String s) {
        String t = s.trim();//trim()去掉字符串首尾的空格
        if (t.length() == 0)
            return 0;
        return t.split("\\s+").length;//split()的参数是正则表达式规则,\\s表示空白,+表示可有多个
    }
}

//Learn from discuss on 20171010
//Time:O(n)
//Space:O(1)
//String
public int countSegments(String s) {
    return ("x " + s).split(" +").length - 1;
}

public class _434_Number_of_Segments_in_a_String {
    public static void main(String[] args) {
        Solution S = new Solution();
        System.out.println(S.countSegments("  Hello, my name is John"));
    }
}
