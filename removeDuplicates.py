# -*- coding: utf-8 -*-


class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) < 1:
            return 0
        if len(nums) < 2:
            return 1
        value = nums[0]
        for i in nums[1:]:
            if (i == value):
                nums.remove(i)
            else:
                value = i
        return len(nums)


if __name__ == '__main__':
    nums = [1, 1, 2, 2, 3]
    solution = Solution()
    len = solution.removeDuplicates(nums)
    print(len)
