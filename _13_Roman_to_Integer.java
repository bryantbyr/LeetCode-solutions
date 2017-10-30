//_13_Roman_to_Integer.java

//Learn from discuss on 20171030
//Time:O(n)
//Space:O(1)
//String
class Solution {
    public int romanToInt(String s) {
        int sum = 0;
        if (s.indexOf("IV") != -1) sum -= 2;
        if (s.indexOf("IX") != -1) sum -= 2;
        if (s.indexOf("XL") != -1) sum -= 20;
        if (s.indexOf("XC") != -1) sum -= 20;
        if (s.indexOf("CD") != -1) sum -= 200;
        if (s.indexOf("CM") != -1) sum -= 200;
        char c[] = s.toCharArray();
        for (int count = 0; count <= s.length() - 1; count++) {
            if (c[count] == 'M') sum += 1000;
            if (c[count] == 'D') sum += 500;
            if (c[count] == 'C') sum += 100;
            if (c[count] == 'L') sum += 50;
            if (c[count] == 'X') sum += 10;
            if (c[count] == 'V') sum += 5;
            if (c[count] == 'I') sum += 1;
        }
        return sum;
    }
}

public class _13_Roman_to_Integer {
    public static void main(String[] args) {
        Solution S = new Solution();
        System.out.println(S.romanToInt("IV"));
    }
}
