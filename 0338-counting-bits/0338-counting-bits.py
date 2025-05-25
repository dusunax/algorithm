'''
# 문제
- 입력값: n
- 반환: n+1 길이의 배열, 값은 index의 바이너리의 1의 개수

# 풀이방식
- bruteforce
- dp: (Hint2)divide the numbers in ranges + (Hint3)odd/even status

# DP 
- how can we make a result, using small number to build the result of large number
- dp[i >> 1] + (i % 2)
- from 1 to n + 1
'''

class Solution:
    '''
    ## bruteforce
    - TC: O(n)
    - SC: O(n)
    '''
    def countBitsBF(self, n: int) -> List[int]:
        result = [0] * (n + 1)

        for i in range(len(result)):
            result[i] = i.bit_count() 
            # bin(self).count("1") (Python 3.9 or earlier)
            # int.bit_count() (Python 3.10 or later)

        return result
    '''
    ## DP
    - TC: O(n)
    - SC: O(n)
    '''
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)

        for i in range(1, len(dp)):
            dp[i] = dp[i >> 1] + (i % 2)
            
        return dp
