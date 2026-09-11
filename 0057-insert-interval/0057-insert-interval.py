from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        newStart, newEnd = newInterval

        for start, end in intervals:

            # Current interval comes before newInterval
            if end < newStart:
                result.append([start, end])

            # Current interval comes after newInterval
            elif start > newEnd:
                result.append([newStart, newEnd])
                result.extend(intervals[intervals.index([start, end]):])
                return result

            # Overlapping intervals
            else:
                newStart = min(newStart, start)
                newEnd = max(newEnd, end)

        # Add newInterval if it wasn't added yet
        result.append([newStart, newEnd])

        return result 