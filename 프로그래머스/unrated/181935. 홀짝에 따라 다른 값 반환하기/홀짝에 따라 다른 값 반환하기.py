def solution(n):    
    answer = 0
    if(bool(n%2)):
        for i in range(1,n+1,2):
            answer = answer+i
    else:
        for i in range(2,n+1,2):
            answer = answer + i**2
            
    return answer