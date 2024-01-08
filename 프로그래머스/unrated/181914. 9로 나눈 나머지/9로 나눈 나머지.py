def solution(number):
    answer = 0
    n = str(number)
    for i in n:
        answer += int(i)
    answer = answer % 9
    return answer