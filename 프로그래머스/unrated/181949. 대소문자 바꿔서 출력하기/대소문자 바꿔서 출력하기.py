str = input()

# 문자의 대소문자 구분하기
# - islower: 대소문자 여부를 판별
# - char.upper: 대문자로 변환
# - char.lower: 소문자로 변환
# ex) str.map(e => e.toLowerCase() === e.toLowerCase() ? e.toUpperCase() : e.toLowerCase())
result = ""
for char in str:
    if char.islower():
        result += char.upper()
    else:
        result += char.lower()

print(result)