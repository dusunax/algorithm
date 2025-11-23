'''
## Problem
- return longest common subsequenece's count
- relative order is matters(stable)
  - "ace" and "eca" has 1 LCS.

## DP with LCS

### DP table
- init dp table with 0's
- prev+1 when we find LCS: dp[i][j] = dp[i-1][j-1] + 1
- keep max when if chars are not LCS: dp[i][j] = max(dp[i-1][j], dp[i][j-1])

### use bottom-up approach
- since we know the table size upfront: (text1's len + 1) x (text2's len + 1), iterative DP is cleaner and efficient (no recurision depths.)
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)

        dp_table = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for i in range(0, len1):
            for j in range(0, len2):
                if text1[i-1] == text2[j-1]:
                    dp_table[i][j] = dp_table[i-1][j-1] + 1
                else:
                    dp_table[i][j] = max(dp_table[i-1][j], dp_table[i][j-1])
        
        return dp_table[len1-1][len2-1]
        