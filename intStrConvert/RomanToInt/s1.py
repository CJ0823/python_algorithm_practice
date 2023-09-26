class Solution:
    def romanToInt(self, s: str) -> int:
        ri_map = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}
        q = ''
        ans = 0
        for ch in s:
            q += ch
            if q != "I" and q != "X" and q != "C" and q in ri_map.keys():
                ans += ri_map[q]
                q = ''
            elif len(q) == 3:
                ans += ri_map[q[0]] * 3
            else:
                continue
        return ans

Solution().romanToInt("MCMXCIV")