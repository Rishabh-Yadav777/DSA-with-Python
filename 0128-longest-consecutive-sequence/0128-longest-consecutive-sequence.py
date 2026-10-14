
class Solution:
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0

        for num in numSet:
            # Start counting only from the beginning of a sequence
            if num - 1 not in numSet:
                currentNum = num
                count = 1

                while currentNum + 1 in numSet:
                    currentNum += 1
                    count += 1

                longest = max(longest, count)

        return longest
