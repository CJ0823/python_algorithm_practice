from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        match_map = {
            '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']
        }
        n = len(digits)
        if n == 0:
            return []
        ans = []

        def backtracking(r):
            if len(r) == n:
                return ans.append(r)
            for i in match_map[digits[len(r)]]:
                backtracking(r + i)

        backtracking("")
        return ans