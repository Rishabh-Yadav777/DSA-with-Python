class Solution:
    def reverseBits(self, n: int) -> int:
        n = n & 0xFFFFFFFF
        result = 0

        for i in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1

        # Convert to signed 32-bit integer
        if result >= (1 << 31):
            result -= (1 << 32)

        return result