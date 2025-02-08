'''
# 76. Minimum Window Substring 

solution reference: https://www.algodale.com/problems/minimum-window-substring/

## 주어진 문자열 s에서 문자열 t의 모든 문자를 포함하는 최소 윈도우를 찾아 반환하기 \U0001f525

> 슬라이딩 윈도우, 최소 윈도우 찾기, 문자열의 빈도 추적, t의 모든 문자가 현재 윈도우에 포함되어 있는지 추적

- 윈도우의 오른쪽 끝을 확장하면서, 필요한 모든 문자가 포함되었을 때, 윈도우의 크기를 최소화하기

## 값
- counts: 필요한 문자가 몇 번 등장하는지 추적
- n_included: 윈도우 안에서 t에 필요한 문자 개수 추적
- low, high: 슬라이딩 윈도우의 양 끝
- min_low max_high: 반환값, 슬라이딩 윈도우의 양 끝

## s 탐색
- s의 오른쪽 끝을 탐색합니다.
  - 현재 문자가 t에 존재한다면(counts에 키가 존재)
    - 그리고 필요한 문자라면(값이 1 이상)
        - 윈도우 내부의 필요 문자 개수를 하나 증가시킵니다.
    - 해당 문자의 등장 count를 하나 감소시킵니다.

## 윈도우 축소하기
- 아래 문항을 필요한 값이 윈도우 안에 존재하는 동안 반복합니다.
1. 현재 구한 윈도우가 더 작은 지 확인하고, 작다면 반환할 윈도우를 업데이트 합니다.
2. s의 왼쪽 끝을 탐색합니다.
  - 현재 문자가 t에 존재한다면(counts에 키가 존재)
    - 해당 문자의 등장 count를 하나 증가시킵니다.
    - 그리고 필요한 문자라면(값이 1 이상)
        - 윈도우 내부의 필요 문자 개수를 하나 축소시킵니다.(반복문의 조건을 벗어납니다.)
3. 다음 탐색 전 왼쪽 위치를 하나 증가시킵니다.

## 반환
- 최소 윈도우의 시작과 끝을 low와 high + 1로 반환하되, 유효한 윈도우가 아니라면 ""을 반환합니다.
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_low = 0
        max_high = len(s)
        counts = Counter(t)
        n_included = 0

        low = 0
        # s 탐색
        for high in range(len(s)):
            char_high = s[high]
            if char_high in counts: 
                if counts[char_high] > 0:
                    n_included += 1
                counts[char_high] -= 1

            # 윈도우 축소하기
            while n_included == len(t):
                if high - low < max_high - min_low: # 1
                    min_low = low
                    max_high = high
                    
                char_low = s[low] 
                if char_low in counts: # 2
                    counts[char_low] += 1
                    if counts[char_low] > 0:
                        n_included -= 1

                low += 1 # 3
            
        return s[min_low: max_high + 1] if max_high < len(s) else "" 
