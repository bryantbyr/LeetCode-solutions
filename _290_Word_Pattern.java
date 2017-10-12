//_290_Word_Pattern.java

import java.util.HashMap;
import java.util.Map;

//Created by bryantbyr on 20171012
//Time:O(n)
//Space:O(n)
//Hash Table
class Solution {
    public boolean wordPattern(String pattern, String str) {
        String[] s = str.split(" ");
        if (s.length != pattern.length())
            return false;
        Map map = new HashMap<>();
        for (Integer i = 0; i < s.length; ++i ) {
            if (map.put(pattern.charAt(i), i) != map.put(s[i], i))
                return false;
        }
        return true;
    }
}

//Created by bryantbyr on 20171012
//Time:O(n)
//Space:O(n)
//Hash Table
class Solution {
    public boolean wordPattern(String pattern, String str) {
        String[] s = str.split(" ");
        if (s.length != pattern.length())
            return false;
        Map<Character, Integer> m1 = new HashMap<>();
        Map<String, Integer> m2 = new HashMap<>();
        for (Integer i = 0; i < s.length; ++i ) {
            if (m1.get(pattern.charAt(i)) != m2.get(s[i]))
                return false;
            m1.put(pattern.charAt(i), i);
            m2.put(s[i], i);
        }
        return true;
    }
}



public class _290_Word_Pattern {
    public static void main(String[] args) {
        Solution S = new Solution();
        System.out.println(S.wordPattern("abba", "dog cat cat dog"));
    }
}
