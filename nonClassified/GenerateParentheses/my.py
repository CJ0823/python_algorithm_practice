from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 3 = (3 x 1) + (2 x 1 + 1 x 1) + (1 x 1 + 2 x 1) + (1 x 3)
        # 4 = (4 x 1) + (3 x 1 + 1 x 1) + (2 x 1 + 2 x 1) + (1 x 1 + 3 x 1) + (1 x 4)
        def getP(n: int):
            return "(" * n + ")" * n if n > 0 else ""

        ans = []
        idx = n
        while idx:
            i = n - idx
            ans.append(getP(idx) + getP(i))
            if (getP(idx) + getP(i)) != getP(i) + getP(idx):
                ans.append(getP(i) + getP(idx))
            idx -= 1
        return ans

