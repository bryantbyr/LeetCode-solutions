//_438_Find_All_Anagrams_in_a_String.java

import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Map.Entry;

//Created by bryantbyr on 20171013
//Time:O(n)
//Space:O(n)
//Hash Table (Time Limit Exceeded)
// class Solution {
//     public List<Integer> findAnagrams(String s, String p) {
//         List<Integer> res = new ArrayList<>();
//         int n = p.length();
//         HashMap<Character, Integer> m = new HashMap<>();
//         for (int i = 0; i < n ; ++i) {
//             if (m.containsKey(p.charAt(i)))
//                 m.put(p.charAt(i), m.get(p.charAt(i)) + 1);
//             else
//                 m.put(p.charAt(i), 0);
//         }
//         for (int i = 0; i < s.length() - n + 1 ; ++i) {
//             HashMap<Character, Integer> map = new HashMap<>();
//             for (int j = i; j < i + n; ++j) {
//                 if (map.containsKey(s.charAt(j)))
//                     map.put(s.charAt(j), map.get(s.charAt(j)) + 1);
//                 else
//                     map.put(s.charAt(j), 0);
//             }
//             for (Entry<Character, Integer> entry : m.entrySet()) {
//                 if (map.containsKey(entry.getKey()) && map.get(entry.getKey()) == entry.getValue())
//                     map.remove(entry.getKey(), entry.getValue());
//             }
//             if (map.isEmpty())
//                 res.add(i);
//         }
//         return res;
//     }
// }

//Learn from discuss on 20171013
//Time:O(n)
//Space:O(n)
//Hash Table + Sliding Window
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> res = new ArrayList<>();
        if (s == null || s.length() == 0 || p == null || p.length() == 0)
            return list;
        int[] hash = new int[256];
        for (char c : p.toCharArray()) {
            hash[c]++;
        }
        int left = 0, right = 0, count = p.length();
        while (right < s.length()) {
            if (hash[s.charAt(right++)]-- >= 1)
                count--;
            if (count == 0)
                res.add(left);
            if (right - left == p.length() && hash[s.charAt(left++)]++ >= 0)
                count++;
        }
        return res;
    }
}


//Created by bryantbyr on 20171013
//Time:O(n)
//Space:O(n)
//Hash Table (Time Limit Exceeded)
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> res = new ArrayList<>();
        if (p == null || s == null || s.length() < p.length())
            return res;
        int n = p.length();
        for (int i = 0; i < s.length() - n + 1 ; ++i) {
            int[] hash = new int[256];
            for (char c : p.toCharArray())
                hash[c]++;
            int j = i;
            for (; j < i + n; ++j) {
                hash[s.charAt(j)]--;
                if (hash[s.charAt(j)] < 0)
                    break;
            }
            if (j < i + n && hash[s.charAt(j)] < 0)
                continue;
            res.add(i);
        }
        return res;
    }
}

public class _438_Find_All_Anagrams_in_a_String {
    public static void main(String[] args) {
        Solution S = new Solution();
        String s = "cbaebabacd", t = "abc";
        List<Integer> r = S.findAnagrams(s, t);
        for (int i = 0; i < r.size(); ++i)
            System.out.println(r.get(i));
    }
}
