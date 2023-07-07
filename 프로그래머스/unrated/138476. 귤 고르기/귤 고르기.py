# Python 기초 익히기
def solution(k, tangerine):
    # 파이썬 리스트 만들기: [초기값] * 리스트 길이
    sizeCount = [0] * (max(tangerine) + 1)

    # 귤 인덱스에 맞춰 갯수 세기
    # 파이썬 for문: for i in range(리스트 길이):
    for i in range(len(tangerine)):
        current = tangerine[i]
        sizeCount[current] += 1

    # 파이썬 내림차순 정렬: sort(reverse=True), 기본값 reverse=False
    # 특이한 점 > 메소드가 두 가지
    # - sort(): sort in place
    # - sorted(): returns sorted array, 원본 리스트는 그대로
    sizeCount.sort(reverse=True) 

    # k만큼 고르기
    index = 0
    answer = 0
    while k > 0:
        k -= sizeCount[index]
        answer += 1
        index += 1

    return answer