'''
## 문제
- 입력값: n
- 반환: n+1 길이의 배열, 값은 index의 바이너리의 1의 개수

## 풀이방식
- bruthforce
- divide the numbers in ranges
- odd/even status

## 
'''

class Solution:
    '''
    ## Bruthforce
    - TC: O(n)
    - SC: O(n)
    '''
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)

        for i in range(len(result)):
            result[i] = i.bit_count() 
            # bin(self).count("1") (Python 3.9 or earlier)
            # int.bit_count() (Python 3.10 or later)

        return result



    # '''
    # ## DP
    # - 이전 계산 결과 기억하기
    
    # ### 풀이
    # ```
    # 이진수 = (이진수 >> 1) + (이진수 & 1)
    # ```
    # - `i >> 1`: i의 비트를 오른쪽으로 1비트 이동(맨 오른쪽 한 칸 버림), `i // 2`와 같음
    # - `i & 1`: `i`의 마지막 비트가 1인지 확인 (1이면 1 추가, 0이면 패스)
    # '''
    # def countBits(self, n: int) -> List[int]:
    #     dp = [0] * (n + 1)
        
    #     for i in range(1, n + 1):
    #         dp[i] = dp[i >> 1] + (i & 1) 
            
    #     return dp