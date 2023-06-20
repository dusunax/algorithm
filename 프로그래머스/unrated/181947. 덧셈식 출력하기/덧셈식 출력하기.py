a, b = map(int, input().strip().split(' '))

# 1. 문자열 출력
# 변수 a, "+", 변수 b, "=", a + b를 구분하여 출력
# print(a, "+", b, "=", a + b)

# 2. f-string: 문자열 포맷팅
# f-string을 사용하여 변수 a, b, a + b를 `문자열에 삽입`하여 출력

# 출력방식: {} 내에 변수, 식을 넣으면 값을 평가하여 출력
# ex) ES6 템플릿 리터럴(Template Literal) => `${a} + ${b} = ${a + b}`
# print(f"{a} + {b} = {a + b}")

# 3. format() 메소드 사용
# format() 메소드를 사용하여 변수 a, b, a + b를 `문자열에 삽입`하여 출력

# 출력방식: {}에 변수를 순서대로 삽입 
# ex) C언어 => printf("%d + %d = %d\n", a, b, a + b);
print("{} + {} = {}".format(a, b, a + b))