# -*- coding: utf-8 -*-
# @Time    : 2019/2/26
# @Author  : qirui
# @FileName: 84. Largest Rectangle in Histogram.py

# reference:    https://www.geeksforgeeks.org/largest-rectangle-under-histogram/
# stack
# 栈内存放数组下标, 对应的高度以此递增。遍历数组, 当遍历到的高度大于栈顶高度即栈内最大高度时,入栈(为使矩形的宽尽可能大); 否则, 弹出栈顶元素, 计算以该栈顶为高度矩形的最大面积。数组内每个值都有机会当矩形的高, 且矩形宽也是最大可能值, 所以可求得最大面积。
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        stack, index, max_area = [], 0, 0
        while index < len(heights):
            if not stack or heights[index] >= heights[stack[-1]]:
                stack.append(index)
                index += 1
            else:
                top_of_stack = stack.pop()
                area = heights[top_of_stack] * (index - stack[-1] - 1 if stack else index)  # stack栈底元素为高时的矩形宽度是index
                max_area = max(max_area, area)

        while stack:
            top_of_stack = stack.pop()
            area = heights[top_of_stack] * ((index - stack[-1] - 1) if stack else index)    # stack栈底元素为高时的矩形宽度是index
            max_area = max(max_area, area)

        return max_area


if __name__ == '__main__':
    S = Solution()
    print(S.largestRectangleArea([6, 3, 4, 6]))
