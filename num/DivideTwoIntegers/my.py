class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a_div = abs(dividend)
        a_dis = abs(divisor)
        count = 0
        if a_div == a_dis:
            return 1 if dividend * divisor > 0 else -1
        while a_div > a_dis:
            a_div -= a_dis
            count += 1
        return count if dividend * divisor > 0 else -1 * count