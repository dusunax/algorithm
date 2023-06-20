str = input()


# 1. 리스트 컴프리헨션과 join 메소드를 사용하여 출력
# - 개행문자 '\n'을 기준로 하여 join()
print('\n'.join([char for char in str]))

# 2. 리스트 컴프리헨션과 언패킹을 사용하여 출력
# generator object, 문자열 => 각 문자를 요소로 하는 1차원 리스트 matrix
matrix = [[char] for char in str]

# - *는 iterable를 언패킹
#   => unpacking을 하지 않을 시, 다음과 같이 출력
#     ['a']
#     ['b']
#     ['c']
#     ['d']
#     ['e']
# ex) ES6 spread 문법 
# for row in matrix:
#     print(*row)