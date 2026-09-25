class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        heights = [0] * cols
        max_area = 0

        for i in range(rows):
            # Current row ko histogram me convert karna
            for j in range(cols):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            # Largest rectangle in histogram
            stack = [-1]

            for j in range(cols):
                while stack[-1] != -1 and heights[j] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    width = j - stack[-1] - 1
                    max_area = max(max_area, h * width)

                stack.append(j)

            # Remaining elements process karna
            while stack[-1] != -1:
                h = heights[stack.pop()]
                width = cols - stack[-1] - 1
                max_area = max(max_area, h * width)

        return max_area 