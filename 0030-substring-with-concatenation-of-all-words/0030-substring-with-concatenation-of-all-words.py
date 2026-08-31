class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        # Frequency of each word
        target = {}

        for word in words:
            target[word] = target.get(word, 0) + 1

        result = []

        # Try each possible starting offset
        for offset in range(word_len):

            left = offset
            count = 0
            window = {}

            for right in range(offset, len(s) - word_len + 1, word_len):

                word = s[right:right + word_len]

                # Word is not in words
                if word not in target:
                    window.clear()
                    count = 0
                    left = right + word_len
                    continue

                # Add word to window
                window[word] = window.get(word, 0) + 1
                count += 1

                # Too many occurrences of this word
                while window[word] > target[word]:
                    left_word = s[left:left + word_len]
                    window[left_word] -= 1
                    left += word_len
                    count -= 1

                # All words are present
                if count == word_count:
                    result.append(left)

                    # Move window forward
                    left_word = s[left:left + word_len]
                    window[left_word] -= 1
                    left += word_len
                    count -= 1

        return result 