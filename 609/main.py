from collections import defaultdict


class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        dupes = defaultdict(list)
        for dr in paths:  # as in dir representation
            tokens = dr.split(" ")
            dname = tokens[0]
            for fr in tokens[1:]:  # as in file representation
                i = fr.rfind("(")
                fname = fr[:i]
                content = fr[i : len(fr)]
                dupes[content].append(f"{dname}/{fname}")

        return [l for l in dupes.values() if len(l) > 1]
