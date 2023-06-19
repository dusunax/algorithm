def solution(price):
    discount = [5, 10, 20]

    if price >= 50 * 10000:
        answer = price * (1 - discount[2] / 100)
    elif price >= 30 * 10000:
        answer = price * (1 - discount[1] / 100)
    elif price >= 10 * 10000:
        answer = price * (1 - discount[0] / 100)
    else:
        answer = price

    return int(answer)
