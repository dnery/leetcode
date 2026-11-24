def _gcd(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    # The GCD between a number and itself is the number itself
    if a == b:
        return a
    # Find greatest common divider using Euclidean algorithm.
    # > https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def _lcm(a: int, b: int) -> int:
    # The LCM between anything and zero is always zero
    if a == 0 or b == 0:
        return 0
    # The LCM between a number and itself is the number itself
    if abs(a) == abs(b):
        return abs(a)
    # The least common MULTIPLE of both numbers is the same
    # as any of them divided by the GCD times the other one.
    the_gcd = _gcd(a, b)
    return abs(a // the_gcd) * abs(b)


class Solution:
    def maxLength(self, nums: list[int]) -> int:
        longest = 0
        for i in range(len(nums)):
            the_lcm = nums[i]
            the_gcd = nums[i]
            the_dot = nums[i]
            # Do the base case outside the nested loop to save 2 function calls.
            # This really isn't necessary at all, bruh.
            if the_dot == the_lcm * the_gcd:
                longest = max(longest, 1)
            for j in range(i + 1, len(nums)):
                the_gcd = _gcd(the_gcd, nums[j])
                the_lcm = _lcm(the_lcm, nums[j])
                the_dot *= nums[j]
                if the_dot == the_lcm * the_gcd:
                    longest = max(longest, j - i + 1)
        return longest
