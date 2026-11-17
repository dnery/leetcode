from collections import defaultdict


def generate_primes(n=123):  # because ord('z') = 122
    primes = []
    candidate = 2
    while len(primes) < n:
        if all(it % candidate != 0 for it in primes):
            primes.append(candidate)
        candidate += 1
    return primes


# Leetcode's Python runtime is smart enough to only run this once
PRIME_LOOKUP = generate_primes()


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Map of lists keyed by string hash
        anagrams = defaultdict(list)

        for word in strs:
            _hash = 1
            # This is equivalent to iterating chars and calling ord()
            for charcode in word.encode("utf-8"):
                _hash *= PRIME_LOOKUP[charcode]
            anagrams[_hash].append(word)

        return list(anagrams.values())
