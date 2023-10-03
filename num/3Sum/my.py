from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        ans.append([nums[i], nums[j], nums[k]])
        return list(set(tuple(sorted(item)) for item in ans))

# Time Limit Exceeded