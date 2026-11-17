class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        fast = 0
        slow = 0
        size = 0
        word = {ch: 0 for ch in s}

        while fast < len(s):
            if word[s[fast]]:
                word[s[slow]] = 0
                slow += 1
                continue

            word[s[fast]] = 1
            fast += 1
            size = max(size, fast - slow)

        return size
