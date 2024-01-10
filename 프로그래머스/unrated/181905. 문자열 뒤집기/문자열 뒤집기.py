def solution(my_string, s, e):
    new = list(my_string[s:e+1])
    new.reverse()
    new = ''.join(new)
    answer = my_string[:s] + new + my_string[e+1:] 
    return answer