# 733. Flood Fill

#Created by bryantbyr on 20181213
#Time:O(N^2)
#Space:O(N)
#DFS
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """

        m, n, start_pixel = len(image), len(image[0]), image[sr][sc]

        def dfs(x, y):
            if x < 0 or x > m - 1 or y < 0 or y > n - 1 or image[x][y] == newColor or image[x][y] != start_pixel:
                return
            image[x][y] = newColor
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)

        dfs(sr, sc)

        return image


if __name__ == '__main__':
    S = Solution()
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(S.floodFill(image, 1, 1, 2))
