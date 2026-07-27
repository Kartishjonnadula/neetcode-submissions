from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []          # stores indices
        maxArea = 0

        # Add a dummy 0-height bar to flush the stack at the end
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]

                # Previous smaller element
                left = stack[-1] if stack else -1

                # Current index is next smaller element
                width = i - left - 1

                maxArea = max(maxArea, h * width)

            stack.append(i)

        return maxArea