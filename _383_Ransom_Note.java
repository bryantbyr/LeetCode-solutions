//_383_Ransom_Note.java
import java.util.Arrays;
import java.util.Map;
import java.util.HashMap;

//Created by bryantbyr on 20171015
//Time:O(n)
//Space:O(n)
//String
class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int[] m1 = new int[256];
        int[] m2 = new int[256];
        for (char c : magazine.toCharArray())
            m2[c]++;
        for (char c : ransomNote.toCharArray()) {
            m1[c]++;
            if (m1[c] > m2[c])
                return false;
        }
        return true;
    }
}

//Created by bryantbyr on 20171015
//Time:O(n)
//Space:O(n)
//String
class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int[] m = new int[256];
        for (char c : magazine.toCharArray())
            m[c]++;
        for (char c : ransomNote.toCharArray()) {
            m[c]--;
            if (m[c] < 0)
                return false;
        }
        return true;
    }
}


//Created by bryantbyr on 20171015
//Time:O(nlog(n))
//Space:O(1)
//String
class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        char[] c1 = ransomNote.toCharArray();
        Arrays.sort(c1);
        char[] c2 = magazine.toCharArray();
        Arrays.sort(c2);
        int i = 0, j = 0;
        for (; i < c2.length && j < c1.length;) {
            if (c1[j] == c2[i]) {
                i++;
                j++;
            } else
                i++;
        }
        return j == c1.length;
    }
}

//Created by bryantbyr on 20171015
//Time:O(nlog(n))
//Space:O(1)
//String
class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        char[] c1 = ransomNote.toCharArray();
        Arrays.sort(c1);
        char[] c2 = magazine.toCharArray();
        Arrays.sort(c2);
        int i = 0, j = 0;
        for (; i < c2.length && j < c1.length;) {
            if (c1[j] == c2[i++])
                j++;
        }
        return j == c1.length;
    }
}

//Learn from discuss on 20171015
//Time:O(nlog(n))
//Space:O(1)
//String
class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        char[] charMag = magazine.toCharArray();
        Arrays.sort(charMag);
        String mag = new String(charMag);
        char[] charRan = ransomNote.toCharArray();
        Arrays.sort(charRan);
        String ran = new String(charRan);
        int index = -1;
        for (int i = 0; i < ran.length(); i++) {
            if (mag.indexOf(ran.charAt(i), index + 1) == -1)
                return false;
            index = mag.indexOf(ran.charAt(i), index + 1);
        }
        return true;
    }
}

//Learn from discuss on 20171015
//Time:O(n)
//Space:O(n)
//String + Hash Table
class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        Map<Character, Integer> magM = new HashMap<>();
        for (char c : magazine.toCharArray()) {
            // int newCount = magM.getOrDefault(c, 0) + 1;
            int newCount = magM.containsKey(c) ? magM.get(c) + 1 : 1;
            magM.put(c, newCount);
        }
        for (char c : ransomNote.toCharArray()) {
            // int newCount = magM.getOrDefault(c, 0) - 1;
            int newCount = magM.containsKey(c) ? magM.get(c) - 1 : -1;
            if (newCount < 0)
                return false;
            magM.put(c, newCount);
        }
        return true;
    }
}

public class _383_Ransom_Note {
    public static void main(String[] args) {
        Solution S = new Solution();
        String s = "aa";
        String t = "aab";
        System.out.println(S.canConstruct(s, t));
    }
}
