class Solution:
    #704 Binary Search
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            c = l + (r - l) // 2
            if nums[c] == target:
                return c
            elif nums[c] < target:
                l = c + 1
            else:
                r = c - 1

        return -1


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    #278 First Bad Version8
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        while l < r:
            c = l + (r - l) // 2
            if isBadVersion(c):
                r = c
            else:
                l = c + 1

        return l

