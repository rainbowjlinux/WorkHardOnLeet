# -*- coding: utf-8 -*-


class Solution(object):
    def twosum(self, nums, target):
        couple = []
        print(nums)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    couple.append([i, j])
                    print("{} + {} = {}".format(nums[i], nums[j], target))
        return couple


if __name__ == '__main__':
    nums = [3, 3, 2, 4]
    target = 6
    solution = Solution()
    couple = solution.twosum(nums, target)
    print(couple)
