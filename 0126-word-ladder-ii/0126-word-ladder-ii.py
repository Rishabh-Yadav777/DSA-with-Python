
from collections import defaultdict

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)

        if endWord not in wordSet:
            return []

        parents = defaultdict(list)
        level = [beginWord]
        visited = {beginWord}
        found = False

        while level and not found:
            nextLevel = set()

            for word in level:
                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        newWord = word[:i] + ch + word[i + 1:]

                        if newWord in wordSet and newWord not in visited:
                            parents[newWord].append(word)
                            nextLevel.add(newWord)

                            if newWord == endWord:
                                found = True

            visited.update(nextLevel)
            level = list(nextLevel)

        if not found:
            return []

        result = []
        path = [endWord]

        def backtrack(word):
            if word == beginWord:
                result.append(path[::-1])
                return

            for parent in parents[word]:
                path.append(parent)
                backtrack(parent)
                path.pop()

        backtrack(endWord)
        return result
