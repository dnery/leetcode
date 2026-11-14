class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        ms = -1

        for i in range(l, len(nums) + 1):
            curr = sum(nums[i - l : i])
            if curr > 0:
                if ms < 0:
                    ms = curr
                ms = min(ms, curr)

            for j in range(i, min(i + r - l, len(nums))):
                curr += nums[j]
                if curr > 0:
                    if ms < 0:
                        ms = curr
                    ms = min(ms, curr)

        return ms
