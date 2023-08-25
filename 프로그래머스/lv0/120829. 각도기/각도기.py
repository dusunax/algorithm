def solution(angle):
    # elif ex) js의 else if
    # elif를 줄이자
    
    # if angle > 0 and angle < 90:
    #     return 1  # 예각
    # if angle == 90:
    #     return 2  # 직각
    # if angle > 90 and angle < 180:
    #     return 3  # 둔각
    # if angle == 180:
    #     return 4  # 평각
    
    # switch
    switch_case = {
        (0 < angle < 90): 1,
        (angle == 90): 2,
        (90 < angle < 180): 3,
        (angle == 180): 4
    }
    
    for condition, degree in switch_case.items():
        if condition:
            return degree