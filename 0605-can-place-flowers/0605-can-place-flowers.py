class Solution:
    '''
    first approach
    '''
    # def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # last_planted = -1
        # for i in range(0, len(flowerbed)-1):
        #     if (
        #         (flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1]) 
        #         and last_planted != i-1
        #     ):
        #         n -= 1
        #         last_planted = i

        #     if n == 0:
        #         return True

        # return False

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(0, len(flowerbed)):
            if flowerbed[i] == 0:
                # for index access errors.
                left_empty = (i == 0 or flowerbed[i-1] == 0)
                right_empty = (i == len(flowerbed)-1 or flowerbed[i+1] == 0)
            
                if left_empty and right_empty:
                    n -= 1
                    flowerbed[i] = 1

                if n == 0:
                    return True

        return n<=0
'''
# Outline
- plant flowers in the plots. no adjacent.
- return Boolean which,
    - true, flower can planted without adjacent plot.
    - false, otherwise

## Approach
- iterate flowerbed once, TC: O(n)
- keep the last pointer where flower's planted, `last_planted`
    - if the prev index value is not 1 and i-1 is 0 and prev - 2 is not last_flower, you can plant it
        - n -= 1, to mark the planting is happen. (no need to update the array it self)
        - update pointer as current index. 
- after the iteration. if n is not 0, you are fail to plant them all. 
  
## 꽃 심기
### 꽃 심기 조건
1. 이전 인덱스 값은 0이어야 한다.
2. 현재 인덱스 값은 1이 아니어야 한다.
3. 마지막에 심은 인덱스는 i-1이 아니어야 한다.

### 꽃 심기 조건이 참일 시
1. 꽃 심을 횟수 n -= 1
2. 마지막에 심은 인덱스 = i

### 꽃 심기 조기종료 조건
n = 0

## Note
- flowerbed is has length more than 0. and they don't have adjacent flowers in them. => no exception for length condition.
- in case of flowerbed is already not able to planted as remaining `n` is bigger than `0` that represent empty plots in flowerbed. can we break the iteration beforehand?
  => No, but do return True, when the flowers are all planted. as satisfies the condition of places all of the flowers.
'''