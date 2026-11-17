# [Minimum Positive Sum Subarray](https://leetcode.com/problems/minimum-positive-sum-subarray?envType=daily-question&envId=2026-11-14)

### [Solution](main.py)

![Submission](submission.png)

### If $`O(n^2)`$ then why fast?

It comes down to the constraints:

- `1 <= nums.length <= 100`
- `1 <= l <= r <= nums.length`
- `-1000 <= nums[i] <= 1000`

The sliding window (r - l) is heavily bounded, so the constant overhead is very low in CPython. This solution is also memory optimal (O(1) space complexity, basically 2 integers) and **therefore is the optimal first choice during an interview.**

### Why $`O(n)`$ sliding window don't work

A standard two-pointer sliding window relies on _monotonicity_ (adding elements always increases the sum, removing elements always decreases it). Because the input contains negative numbers, shrinking the window can increase the sum, breaking two-pointer guarantees.

### What does a runtime optimal approach look like

It involves using a binary-indexed tree (BIT, Fenwick tree) or with prefixed sums index. Runtime complexity shrinks to O(n * log(r - l + 1)), but space complexity increases to O(n). For this specific problem, **the runtime-optimal approach actually performs worse.**

Prefix sum index arrays also contain a downside: the array has to be a sparse implementation or it'll need to be long enough to index the values. To work around that, you can use a **coordinate compression map.** [Read more.](https://docs.google.com/document/d/17MMkuAEyzR5mTJsM_wtmUG6v9nLwx-g694_KGn5ICAU/edit?usp=sharing)

## Timing

- Took many hours on this because I was obsessed with the theoretically optimal version.
- If I had just submitted the trivial implementation I'd also realize that it is the best one because of the tight constraints (`1 <= nums.length <= 100`).
