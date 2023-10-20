class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(": ")", "[": "]", "{": "}"}
        st = []
        for el in s:
            if el in pairs.keys():
                st.append(el)
            else:
                if not st or st and el != pairs[st.pop()]:
                    return False
        if st:
            return False
        return True