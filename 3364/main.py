class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        ms = -1

        for i in range(l, len(nums) + 1):
            # A linear operation up until l, once per outer loop
            curr = sum(nums[i - l : i])
            if curr > 0:
                ms = curr if ms < 0 else min(ms, curr)

            for j in range(i, min(i + r - l, len(nums))):
                # A constant addition of value j, once per inner loop
                curr += nums[j]
                if curr > 0:
                    ms = curr if ms < 0 else min(ms, curr)

        return ms
