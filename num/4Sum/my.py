from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i in range(len(nums) - 3):
            for j in range(i+1, len(nums) - 2):
                start = j + 1
                end = len(nums) - 1
                while start < end:
                    if nums[i] + nums[j] + nums[start] + nums[end] == target:
                        ans.add((nums[i], nums[j], nums[start], nums[end]))
                        start += 1
                    elif nums[i] + nums[j] + nums[start] + nums[end] < target:
                        start += 1
                    else:
                        end -= 1
        return [list(a) for a in ans]

print(Solution().fourSum(nums = [1,0,-1,0,-2,2], target = 0))