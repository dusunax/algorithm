a, b = input().strip().split(' ')
b = int(b)

# 1. 문자열 * 정수

# 문자열을 정수 만큼 반복합니다.
# ex) JS => a.repeat(b);
print(a * b)

# 2. join() 메소드

# 문자열과 join 메소드를 사용하는 경우
# ''.join([a] * b);
# ex) JS => new Array(b).fill(...a).join();
# print(''.join([a] * b))