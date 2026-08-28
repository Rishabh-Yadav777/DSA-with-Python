class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(s, open_count, close_count):
            # A complete valid combination
            if len(s) == 2 * n:
                result.append(s)
                return

            # Add an opening parenthesis
            if open_count < n:
                backtrack(s + "(", open_count + 1, close_count)

            # Add a closing parenthesis
            if close_count < open_count:
                backtrack(s + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result 