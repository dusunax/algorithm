class Solution:
    # Backtracking = find combination
    # candidate is distinct & can use multiple times.
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []  

        def backtrack(currIdx, remain, combination):
            if(remain == 0):
                result.append(combination[:])
                return
            if(remain < 0):
                return

            for i in range(currIdx, len(candidates)):
                combination.append(candidates[i])
                backtrack(i, remain - candidates[i], combination) 
                combination.pop()

        backtrack(0, target, [])
        return result
