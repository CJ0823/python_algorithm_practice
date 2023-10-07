import itertools
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        match_map = {
            '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']
        }
        matched_list = [match_map[s] for s in digits]
        cases = itertools.product(*matched_list)
        return [''.join(ch_list) for ch_list in cases] if matched_list else []