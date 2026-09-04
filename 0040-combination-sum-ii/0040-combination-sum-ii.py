class Solution:
    def combinationSum2(self, candidates, target):

        result = []

        # Sort to handle duplicates easily
        candidates.sort()

        def backtrack(start, current, total):

            # Target mil gaya
            if total == target:
                result.append(current[:])
                return

            # Target exceed ho gaya
            if total > target:
                return

            for i in range(start, len(candidates)):

                # Skip duplicate numbers at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since array is sorted
                if total + candidates[i] > target:
                    break

                # Choose
                current.append(candidates[i])

                # Move to next index
                # Same element dobara use nahi kar sakte
                backtrack(i + 1, current, total + candidates[i])

                # Backtrack
                current.pop()

        backtrack(0, [], 0)

        return result 