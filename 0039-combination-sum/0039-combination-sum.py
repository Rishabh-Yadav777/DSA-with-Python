class Solution:
    def combinationSum(self, candidates, target):

        result = []

        def backtrack(start, current, total):

            # Target achieve ho gaya
            if total == target:
                result.append(current[:])
                return

            # Target exceed ho gaya
            if total > target:
                return

            for i in range(start, len(candidates)):

                # Choose
                current.append(candidates[i])

                # Same number dobara choose kar sakte hain
                backtrack(i, current, total + candidates[i])

                # Undo / Backtrack
                current.pop()

        backtrack(0, [], 0)

        return result 