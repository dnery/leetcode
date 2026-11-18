# [Minimum Number of Changes to Make Binary String Beautiful](https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/description/?envType=daily-question&envId=2026-11-18)

### [Solution](main.py)

![Submission](submission.png)

## It's very stupid actually

Because of the constraints:

- Each substring has an even length.
- Each substring contains only `1`'s or only `0`'s.

For about 90m I was working under the assumption that all substrings must contain the same length, that is, if more than 1, they'd have to section the string perfectly. But no, they just have to be even. Unite that with the fact that the string contains only `0`s and `1`s, and you can solve the problem linearly by simply iterating through pairs:

1. If the pair is equal, don't increment the counter, just go to the next pair.
2. If the pair differs, `+1` and go to the next pair. It doesn't matter which one you change, because there can only be 2 possibilities, either the first or the second, and in either case you increment 1. You don't have to expand the search space with "switch and go to next element", for example, because that would assume that substrings can be uneven, **and they can't.**

A substring of even length can **always** be factored into pairs, and because it can't ever be uneven, the minimum amount of changes needed in a substring will always be the sum of the amount of changes needed in each of it's composing pairs.

**The fact that the value space is binary is a core constraint** because substrings do not have to aware of the values in neighboring substrings. Having more than 2 values would complicate this problem significantly.

**TODO:** how complicated, though?

## Timing

- First version completed in 90m using a memo array.
- I realized then (very late) that this thing doesn't need DP, and rewrote it in ~1m.
