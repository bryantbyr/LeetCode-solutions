//_680_Valid_Palindrome_II.java

//Created by bryantbyr on 20171017
//Time:O(n^2)
//Space:O(n)
//String (Time Limit Exceeded)
// class Solution {
//     public boolean isPalindrome(String s) {
//         return s.equals(new StringBuilder(s).reverse().toString());
//     }
//     public boolean validPalindrome(String s) {
//         if (isPalindrome(s) == true)
//             return true;
//         for (int i = 0; i < s.length() ; ++i) {
//             if (isPalindrome(s.substring(0, i) + s.substring(i + 1)))
//                 return true;
//         }
//         return false;
//     }
// }

//Created by bryantbyr on 20171017
//Time:O(n^2)
//Space:O(n)
//String (Time Limit Exceeded)
// class Solution {
//     public boolean validPalindrome(String s) {
//         if (s.equals(new StringBuilder(s).reverse().toString()))
//             return true;
//         for (int i = 0; i < s.length() ; ++i) {
//             if ((s.substring(0, i) + s.substring(i + 1)).equals(new StringBuilder(s.substring(0, i) + s.substring(i + 1)).reverse().toString()))
//                 return true;
//         }
//         return false;
//     }
// }

//Created by bryantbyr on 20171017
//Time:O(n^2)
//Space:O(1)
//String (Time Limit Exceeded)
// class Solution {
//     public boolean isPalindrome(String s) {
//         int l = 0, r = s.length() - 1;
//         while (l < r) {
//             if (s.charAt(l++) != s.charAt(r--))
//                 return false;
//         }
//         return true;
//     }
//     public boolean validPalindrome(String s) {
//         if (isPalindrome(s) == true)
//             return true;
//         for (int i = 0; i < s.length() ; ++i) {
//             if (isPalindrome(s.substring(0, i) + s.substring(i + 1)))
//                 return true;
//         }
//         return false;
//     }
// }

//Created by bryantbyr on 20171017
//Time:O(n)
//Space:O(1)
//String (Time Limit Exceeded)
class Solution {
    public boolean isPalindrome(String s) {
        int l = 0, r = s.length() - 1;
        while (l < r) {
            if (s.charAt(l++) != s.charAt(r--))
                return false;
        }
        return true;
    }
    public boolean validPalindrome(String s) {
        int l = 0, r = s.length() - 1;
        while (l < r) {
            if (s.charAt(l++) != s.charAt(r--)) {
                if (!isPalindrome(s.substring(l, r + 2)) && !isPalindrome(s.substring(l - 1, r + 1)))
                    return false;
                else
                    return true;
            }
        }
        return true;
    }
}

//Created by bryantbyr on 20171017
//Time:O(n)
//Space:O(1)
//String (Time Limit Exceeded)
class Solution {
    public boolean isPalindrome(String s, int l, int r) {
        while (l < r) {
            if (s.charAt(l++) != s.charAt(r--))
                return false;
        }
        return true;
    }
    public boolean validPalindrome(String s) {
        int l = 0, r = s.length() - 1;
        while (l < r) {
            if (s.charAt(l++) != s.charAt(r--))
                return isPalindrome(s, l, r + 1) || isPalindrome(s, l - 1, r);
        }
        return true;
    }
}

public class _680_Valid_Palindrome_II {
    public static void main(String[] args) {
        Solution S = new Solution();
        System.out.println(S.validPalindrome("acddc"));
    }
}
