# -*- coding: utf-8 -*-


class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        nums[:] = sorted(list(set(nums)))
        return len(nums)


if __name__ == '__main__':
    nums = [1, 1, 2, 2, 3]
    solution = Solution()
    len = solution.removeDuplicates(nums)
    print(len)
