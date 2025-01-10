class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)

        segment_dp = [False] * (n + 1)
        segment_dp[0] = True

        for end in range(1, n + 1):
            for start in range(end):
                if segment_dp[start] and s[start:end] in word_set:
                    segment_dp[end] = True
                    break
        
        return segment_dp[n]

        # Time Limit Exceeded
        # def backtracking(i):
        #     if i == len(s):
        #         return True

        #     for word in wordDict:
        #         word_len = len(word)

        #         if s[i : i + word_len] == word:
        #             if backtracking(i + word_len):
        #                 return True

        #     return False

        # return backtracking(0)
        

                    