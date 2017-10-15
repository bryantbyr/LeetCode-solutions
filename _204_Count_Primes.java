//_204_Count_Primes.java

//Learn from discuss on 20171014
//Time:O(n^2)
//Space:O(n)
//Hash Table
class Solution {
    public int countPrimes(int n) {
        int res = 0;
        boolean[] notPrime = new boolean[n];
        for (int i = 2; i <= Math.sqrt(n) ; ++i) {
            if (notPrime[i])
                continue;
            for (int j = 2; i * j < n ; ++j)
                notPrime[i * j] = true;
        }
        for (int i = 2; i < notPrime.length ; ++i) {
            if (!notPrime[i])
                res++;
        }
        return res;
    }
}

//Learn from discuss on 20171014
//Time:O(n^2)
//Space:O(n)
//Hash Table
class Solution {
    public int countPrimes(int n) {
        int res = 0;
        boolean[] notPrime = new boolean[n];
        for (int i = 2; i < n; ++i) {
            if (!notPrime[i]) {
                res++;
                if (i > Math.sqrt(n))
                    continue;
                for (int j = 2; i * j < n ; ++j)
                    notPrime[i * j] = true;
            }
        }
        return res;
    }
}


public class _204_Count_Primes {
    public static void main(String[] args) {
        Solution S = new Solution();
        System.out.println(S.countPrimes(10));
    }
}
