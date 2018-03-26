# -*- coding: utf-8 -*-


class Solution(object):
    def maxProfit(self, nums):
        maxValue = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                print("{} - {}".format(nums[j], nums[i]))
                if (nums[j] - nums[i] > maxValue):
                    maxValue = nums[j] - nums[i]
        return maxValue


if __name__ == '__main__':
    nums = [7, 1, 5, 6, 2, 3]
    # nums = [7, 6, 5, 4, 3, 2]
    solution = Solution()
    maxprofit = solution.maxProfit(nums)
    print(maxprofit)
