class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0

        while i < len(words):
            # Find how many words can fit in this line
            line_len = len(words[i])
            j = i + 1

            while j < len(words):
                # +1 for the minimum space between words
                if line_len + 1 + len(words[j]) > maxWidth:
                    break

                line_len += 1 + len(words[j])
                j += 1

            line_words = words[i:j]
            total_spaces = maxWidth - sum(len(word) for word in line_words)
            gaps = len(line_words) - 1

            # Last line or line with only one word
            if j == len(words) or gaps == 0:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                # Distribute spaces evenly
                space_each = total_spaces // gaps
                extra = total_spaces % gaps

                line = ""

                for k in range(gaps):
                    line += line_words[k]
                    line += " " * (space_each + (1 if k < extra else 0))

                line += line_words[-1]

            result.append(line)
            i = j

        return result 