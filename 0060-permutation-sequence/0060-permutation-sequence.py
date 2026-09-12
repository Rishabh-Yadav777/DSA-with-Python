class Solution:
    def getPermutation(self, n, k):
        numbers = list(range(1, n + 1))
        result = []

        k -= 1  # Convert k to 0-based indexing

        factorial = 1
        for i in range(1, n):
            factorial *= i

        for i in range(n, 0, -1):
            index = k // factorial
            result.append(str(numbers[index]))
            numbers.pop(index)

            if i > 1:
                k %= factorial
                factorial //= (i - 1)

        return ''.join(result) 