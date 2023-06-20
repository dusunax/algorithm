a, b = map(int, input().strip().split(' '))

# 1. 문자열 + 개행 문자
# print("a =", a, "\nb =", b)

# 2. print를 여러 개 사용
# print("a =", a)
# print("b =", b)

# 3. f-string: 문자열 포맷팅 방법 중 하나 (파이썬 3.6~)
# 문자열 안에 중괄호({})를 사용하여 변수나 표현식을 삽입하는 방식
# 중괄호 안에 변수나 표현식을 넣으면, 실제 값으로 치환하여 문자열을 생성
# ex) 자바스크립트 ES6의 템플릿 리터럴
print(f"a = {a}")
print(f"b = {b}")