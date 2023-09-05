from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    result = []

    def dfs(csum, index, path):
        if csum < 0:
            return
        if csum == 0:
            result.append(path)
            return
        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], i, path + [candidates[i]])

    dfs(target, 0, [])
    return result

#1.
# input candidates = [2,3,6,7], target = 7
# output [[7], [2,2,3]]

#2.
# input candidates = [2,3,5], target = 8
# output [[2,2,2,2], [2,3,3], [3,5]]

combinationSum([2,3,6,7], 7)

'''
stack에 다음 요소로 쌓을 인자를 dfs로 추가한다
재귀일 경우 종료 시점을 고려해야한다
'''