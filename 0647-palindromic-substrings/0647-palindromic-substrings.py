class Solution:
    def countSubstringsDPTable(self, s: str) -> int:
        '''
        A.
        '''
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0

        for i in range(n):
            dp[i][i] = True
            count += 1
        
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                count += 1

        for s_len in range(3, n + 1):
            for i in range(n - s_len + 1):
                j = i + s_len - 1
                
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    count += 1

        return count
    def countSubstrings(self, s: str) -> int:
        '''
        B.
        '''
        count = 0

        def expand(left, right):
            nonlocal count
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        
        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)
        
        return count

        


        
        