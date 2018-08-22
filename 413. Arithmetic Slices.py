#413. Arithmetic Slices

#Created by bryantbyr on 20180822
#Time:O(N)
#Space:O(1)
#math + DP
class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count, result = 2, 0
        for i in range(1, len(A) - 1):
            if 2 * A[i] == A[i + 1] + A[i - 1]:
                count += 1
            else:
                result += count * (count - 3) / 2 + 1
                count = 2
        result += count * (count - 3) / 2 + 1
        return result


S = Solution()
print(S.numberOfArithmeticSlices([1, 2, 3, 4, 5, 6]))
