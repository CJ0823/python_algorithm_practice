class Solution:
    def intToRoman(self, num: int) -> str:
        # create a list of lists containing pair of integer and its roman value
        # including special cases like XC = 90
        SymList = [
            ['I', 1],
            ['IV', 4],
            ['V', 5],
            ['IX', 9],
            ['X', 10],
            ['XL', 40],
            ['L', 50],
            ['XC', 90],
            ['C', 100],
            ['CD', 400],
            ['D', 500],
            ['CM', 900],
            ['M', 1000]
        ]

        # to retrun later as answer
        res = []

        # iterate thorough SymList in reverse order i.e start from largest number (M)
        for str, val in reversed(SymList):

            # count will tell us how many times letter has to add in result string
            # i.e 'M' for 1000 and' MM' for 2000
            count = num // val
            # if count is greater than zero
            if count:
                # add that many letters to result array
                res.append(str * count)
                # update our input num
                num %= val

        # convert result array into string and return
        return ''.join(res)