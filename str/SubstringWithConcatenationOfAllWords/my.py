from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from copy import deepcopy

        ans = []
        for word in words:
            candid = s.find(word) # several candid can be
            if candid != -1:
                candid_s = s[candid + len(word) - 1:]
                testing_words_list = deepcopy(words)
                testing_words_list.remove(word)
                try_count = len(testing_words_list)
                while try_count > 0:
                    tester = testing_words_list[0]
                    if candid_s[:len(tester)] == tester:
                        testing_words_list.remove(tester)
                    else:
                        testing_words_list.remove(tester)
                        testing_words_list.append(tester)
                    try_count -= 1
                if not testing_words_list:
                    ans.append(candid)

Solution().findSubstring("barfoothefoobarman", ["foo","bar"])