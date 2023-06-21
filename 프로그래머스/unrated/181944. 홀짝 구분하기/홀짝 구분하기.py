a = int(input())

# 1. format 메소드
# print('{} is {}'.format(a, "even" if a % 2 == 0 else "odd"))

# 2. f-string 템플릿
# if else문
if a % 2 == 0:
    result = "even"
else:
    result = "odd"
    
# print(f'{a} is {result}')
    
# 3. dict 자료형을 사용한 출력
# ex) 자바스크립트의 object
result_dict = {True: "even", False: "odd"}
print(f'{a} is {result_dict[a % 2 == 0]}')