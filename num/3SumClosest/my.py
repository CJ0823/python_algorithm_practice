import sys
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = sys.maxsize
        nums.sort()
        for i in range(len(nums) - 2):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                new_ans = nums[i] + nums[start] + nums[end]
                if abs(new_ans - target) < abs(ans - target):
                    ans = new_ans
                    if new_ans < 0:
                        start += 1
                    elif new_ans > 0:
                        end -= 1
                    else:
                        break
                else:
                    start += 1
        return ans

Solution().threeSumClosest(nums=[-1,2,1,-4], target=1)

# Wrong Case
'''
Input
nums = [4,0,5,-5,3,3,0,-4,-5]
target = -2
Output = -4
Expected = -2
'''
