from collections import defaultdict


def generate_primes(n: int = 123) -> list[int]:
    # n=122 because ord('z')=122
    primes = []
    candidate = 2
    while len(primes) < n:
        # if primes is empty, all(...) evaluates to True
        if all(candidate % it != 0 for it in primes):
            primes.append(candidate)
        candidate += 1
    return primes


# Leetcode seems smart enough to _not_ run global computation
# (such as PRIME_LOOKUP definition) on every test case, i.e.
# PRIME_LOOKUP seems to be computed only once, because this
# beats the trivial string sorting approach by almost 20ms.
PRIME_LOOKUP = generate_primes()


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Map of lists keyed by string hash
        anagrams = defaultdict(list)
        for word in strs:
            _hash = 1
            # The below is equivalent to iterating chars and calling ord(),
            # but marginally faster because the encoding step happens
            # only once per string. I don't think the difference is
            # significant though.
            for ch in word.encode("utf-8"):
                _hash *= PRIME_LOOKUP[ch]
            anagrams[_hash].append(word)
        return list(anagrams.values())
