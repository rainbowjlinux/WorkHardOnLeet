# -*- coding: utf-8 -*-


class Solution(object):
    def twosum(self, nums, target):
        d = dict()
        for index, value in enumerate(nums):
            m = target - value
            if m in d:
                return d[m], index
            else:
                d[value] = index


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    ans = solution.twosum(nums, target)
    print(ans)
