class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        pal = [[False] * n for _ in range(n)]
        cuts = [0] * n

        for end in range(n):
            cuts[end] = end

            for start in range(end + 1):
                if s[start] == s[end] and (
                    end - start <= 2 or pal[start + 1][end - 1]
                ):
                    pal[start][end] = True

                    if start == 0:
                        cuts[end] = 0
                    else:
                        cuts[end] = min(
                            cuts[end], cuts[start - 1] + 1
                        )

        return cuts[n - 1]