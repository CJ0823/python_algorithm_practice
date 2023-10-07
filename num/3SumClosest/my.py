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
                    if new_ans < target:
                        start += 1
                    elif new_ans > target:
                        end -= 1
                    else:
                        break
                else:
                    if new_ans < target:
                        start += 1
                    elif new_ans > target:
                        end -= 1
                    else:
                        break
        return ans