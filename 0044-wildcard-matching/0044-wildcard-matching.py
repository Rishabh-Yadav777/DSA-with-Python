class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)

        # dp[i][j] = whether s[:i] matches p[:j]
        dp = [[False] * (m + 1) for _ in range(n + 1)]

        # Empty string matches empty pattern
        dp[0][0] = True

        # Empty string can match a pattern containing only '*'
        for j in range(1, m + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                if p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    # Current characters match
                    dp[i][j] = dp[i - 1][j - 1]

                elif p[j - 1] == '*':
                    # '*' matches:
                    # 1. Empty sequence
                    # 2. One or more characters
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

        return dp[n][m] 