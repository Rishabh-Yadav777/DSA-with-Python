from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        words = set(wordDict)

        @lru_cache(None)
        def solve(start):
            if start == len(s):
                return [""]

            ans = []

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word in words:
                    for rest in solve(end):
                        if rest:
                            ans.append(word + " " + rest)
                        else:
                            ans.append(word)

            return ans

        return solve(0)