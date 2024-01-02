def solution(my_string, k):
    answer = ''
    for i in range(k):
        answer= answer + my_string
    return answer
    #return my_string*k