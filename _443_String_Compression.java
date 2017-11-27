
//Created by bryantbyr on 20171127
//Time:O(n)
//Space:O(1)
//String
class Solution {
    public int compress(char[] chars) {
        int cnt = 1;
        int lastIndex = 0;
        //Arrays.sort(chars);
        int i = 1;
        for (; i < chars.length; i++ ) {
            if (chars[i] == chars[i - 1])
                cnt++;
            else {
                if (cnt == 1)
                    chars[lastIndex++] = chars[i - 1];
                else {
                    String str =  String.valueOf(cnt);//int->String
                    chars[lastIndex++] = chars[i - 1];
                    for (int j = 0; j < str.length(); j++)
                        chars[lastIndex++] = str.charAt(j);
                    cnt = 1;
                }
            }
        }
        if (cnt == 1)
            chars[lastIndex++] = chars[i - 1];
        else {
            String str =  String.valueOf(cnt);
            chars[lastIndex++] = chars[i - 1];
            for (int j = 0; j < str.length(); j++)
                chars[lastIndex++] = str.charAt(j);
        }
        return lastIndex;
    }
}

//Learn from discuss on 20171127
//Time:O(n)
//Space:O(1)
//String
class Solution {
    public int compress(char[] chars) {
        int indexAns = 0;
        for (int i = 0; i < chars.length;) {
            int count = 0;
            char temp = chars[i];
            while (i < chars.length && chars[i] == temp) {
                i++;
                count++;
            }
            chars[indexAns++] = temp;
            if (count != 1) {
                for (char c : Integer.toString(count).toCharArray())
                    chars[indexAns++] = c;
            }
        }
        return indexAns;
    }
}

public class _443_String_Compression {
    public static void main(String[] args) {
        char[] chars = {'a', 'b', 'c'};
        Solution s = new Solution();
        System.out.println(s.compress(chars));
    }
}
