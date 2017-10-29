//_583_Delete_Operation_for_Two_Strings.java

//Learn from discuss on 20171029
//Time:O(n^2)
//Space:O(n^2)
//DP + String
class Solution {
    public int minDistance(String word1, String word2) {
        int[][] dp = new int[word1.length() + 1][word2.length() + 1];
        for (int i = 0; i <= word1.length() ; ++i) {
            for (int j = 0; j <= word2.length() ; ++j) {
                if (i == 0 || j == 0)
                    dp[i][j] = 0;
                else
                    dp[i][j] = (word1.charAt(i - 1) == word2.charAt(j - 1)) ? dp[i - 1][j - 1] + 1 :
                               Math.max(dp[i][j - 1], dp[i - 1][j]);
            }
        }
        int com = dp[word1.length()][word2.length()];
        return word1.length() + word2.length() - 2 * com;
    }
}

public class _583_Delete_Operation_for_Two_Strings {
    public static void main(String[] args) {
        Solution S = new Solution();
        String s1 = "sea";
        String s2 = "eat";
        System.out.println(S.minDistance(s1, s2));
    }
}
