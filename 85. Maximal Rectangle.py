# -*- coding: utf-8 -*-
# @Time    : 2019/2/26
# @Author  : qirui
# @FileName: 85. Maximal Rectangle.py

# reference:    https://leetcode.com/problems/maximal-rectangle/discuss/29064/A-O(n2)-solution-based-on-Largest-Rectangle-in-Histogram
# stack + DP
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        row, column = len(matrix), len(matrix[0])
        heights = [0 for _ in range(column)]
        max_area, stack = 0, []
        for i in range(row):
            for j in range(column):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            index = 0
            while index < column:
                if not stack or heights[index] >= heights[stack[-1]]:
                    stack.append(index)
                    index += 1
                else:
                    top_of_stack = stack.pop()
                    area = heights[top_of_stack] * (index - stack[-1] - 1 if stack else index)
                    max_area = max(max_area, area)
            while stack:
                top_of_stack = stack.pop()
                area = heights[top_of_stack] * (index - stack[-1] - 1 if stack else index)
                max_area = max(max_area, area)
        return max_area


# reference:    https://leetcode.com/problems/maximal-rectangle/discuss/29054/Share-my-DP-solution
# DP
# 1.height[i]: 第i列的最大高度; left[i]: 第i列最大高度height[i]对应矩形的最左边界; right[i]: 第i列最大高度height[i]对应矩形的最右边界;
# 2.height[i] = height[i]+1 or 0; left[i]=max(left[i],cur_left); right[i]=max(right[i],cur_right)
#   area = (right[j] - left[j]) * heights[j])
# 遍历每一行, 每行的每个最大高度对应的矩形面积都会考虑到
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        row, column = len(matrix), len(matrix[0])
        heights = [0 for _ in range(column)]
        left = [0 for _ in range(column)]
        right = [column for _ in range(column)]
        max_area = 0

        for i in range(row):
            # compute height
            for j in range(column):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            # compute left
            cur_left = 0
            for j in range(column):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1
            # compute right
            cur_right = column
            for j in range(column - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = column
                    cur_right = j
            # compute area of height[j] at row i
            for j in range(column):
                max_area = max(max_area, (right[j] - left[j]) * heights[j])

        return max_area


if __name__ == '__main__':
    S = Solution()
    print(S.maximalRectangle([["0", "1", "1", "0", "1"],
                              ["1", "1", "0", "1", "0"],
                              ["0", "1", "1", "1", "0"],
                              ["1", "1", "1", "1", "0"],
                              ["1", "1", "1", "1", "1"],
                              ["0", "0", "0", "0", "0"]]))
