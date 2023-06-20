def solution(my_string, overwrite_string, s):
    # 문자열 자르기
    # - string[:index]: 문자열을 index 앞까지 자름
    # - string[index:]: 문자열을 index 뒤까지 자름
    
    # JavaScript => my_string.replce(my_string.indexOf('s'), overwrite_string)
    
    # 문자열의 s 인덱스 이전 + overwrite_string + s 인덱스 이후부터 끝
    return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]
