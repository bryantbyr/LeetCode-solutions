//_38_Count_and_Say.java

//Created by bryantbyr on 20171015
//Time:O(n)
//Space:O(1)
//String
class Solution {
    public String countAndSay(int n) {
        String S = new String("1");
        for (int i = 2; i <= n; ++i) {
            String builder = "";
            for (int index = 1; index < S.length(); ++index) {
                int count = 1;
                while (index < S.length() && S.charAt(index) == S.charAt(index - 1)) {
                    count++;
                    index++;
                }
                builder = builder + count + S.charAt(index - 1);//Way 1 to concat!

                // builder = builder.concat(String.valueOf(count));
                // builder = builder.concat(String.valueOf(S.charAt(index - 1)));//way 2 to concat!

                // builder = builder.concat(String.valueOf(count));
                // builder = builder + S.charAt(index - 1);//way 3 to concat!
                if (index == S.length() - 1 && S.charAt(index) != S.charAt(index - 1))
                    builder += "1" + S.charAt(index);
            }
            if (S.length() == 1)
                S = "11";
            else
                S = builder;
        }
        return S;
    }
}

//Created by bryantbyr on 20171015
//Time:O(n)
//Space:O(1)
//String (Better Control)
class Solution {
    public String countAndSay(int n) {
        String S = new String("1");
        for (int i = 2; i <= n; ++i) {
            String builder = "";
            int count = 1;
            int index = 1;
            for (; index < S.length(); ++index) {
                if (S.charAt(index) == S.charAt(index - 1)) {
                    count++;
                } else {
                    builder = builder + count + S.charAt(index - 1);//Way 1 to concat!
                    count = 1;
                }
            }
            builder = builder + count + S.charAt(index - 1);//Way 1 to concat!
            S = builder;
        }
        return S;
    }
}

//Learn from discuss on 20171015
//Time:O(n)
//Space:O(1)
//String (Better Concat)
class Solution {
    public String countAndSay(int n) {
        String S = new String("1");
        for (int i = 2; i <= n; ++i) {
            StringBuilder builder = new StringBuilder();
            int count = 1;
            int index = 1;
            for (; index < S.length(); ++index) {
                if (S.charAt(index) == S.charAt(index - 1)) {
                    count++;
                } else {
                    builder.append(count).append(S.charAt(index - 1));
                    count = 1;
                }
            }
            builder.append(count).append(S.charAt(index - 1));
            S = builder.toString();
        }
        return S;
    }
}

//Learn from discuss on 20171015
//Time:O(n)
//Space:O(1)
//String (Better Concat)
class Solution {
    public String countAndSay(int n) {
        String S = new String("1");
        StringBuilder builder = new StringBuilder();
        for (int i = 2; i <= n; ++i) {
            int count = 1;
            int index = 1;
            for (; index < S.length(); ++index) {
                if (S.charAt(index) == S.charAt(index - 1)) {
                    count++;
                } else {
                    builder.append(count).append(S.charAt(index - 1));
                    count = 1;
                }
            }
            builder.append(count).append(S.charAt(index - 1));
            S = builder.toString();
            builder.setLength(0);
        }
        return S;
    }
}

public class _38_Count_and_Say {
    public static void main(String[] args) {
        Solution S = new Solution();
        System.out.println(S.countAndSay(6));
    }
}
