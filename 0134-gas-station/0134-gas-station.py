class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        curr_gas = 0
        start = 0

        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            curr_gas += gas[i] - cost[i]

            if curr_gas < 0:
                start = i + 1
                curr_gas = 0

        if total_gas < 0:
            return -1

        return start