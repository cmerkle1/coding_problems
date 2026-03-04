'''Given an array of integers num and an integer target, return
indices of the two numbers such that they add up to target.'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

my_solution = Solution()
answer = my_solution.twoSum([1, 2, 3, 4, 7], 9)
print(answer)
