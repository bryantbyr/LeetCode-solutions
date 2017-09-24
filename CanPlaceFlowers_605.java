//CanPlaceFlowers_605.java

//Created by bryantbyr on 20170924
//Time:O(n)
//Space:O(1)
//array
class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        for (int i = 0; i < flowerbed.length ; ++i ) {
            if ((i == 0 || flowerbed[i - 1] == 0) && flowerbed[i] == 0 && (i == flowerbed.length - 1 || flowerbed[i + 1] == 0)) {
                n--;
                i++;
            }
            if (n <= 0)
                return true;
        }
        return false;
    }
}


public class CanPlaceFlowers_605 {
    public static void main(String[] args) {
        int[] nums = {1, 0, 0, 0, 0, 1};
        Solution S = new Solution();
        System.out.println(S.canPlaceFlowers(nums, 1));
    }
}
