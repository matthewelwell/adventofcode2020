from math import gcd


def lcm(*nums):
    lcm = nums[0]

    for i in nums[1:]:
      lcm = lcm * i//gcd(lcm, i)

    return lcm
