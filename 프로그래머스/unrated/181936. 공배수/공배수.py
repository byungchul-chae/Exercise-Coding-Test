def solution(number, n, m):
    if((number%m or number%n) == 0):
        return 1
    else:
        return 0
    #return 1 if number%n==0 and number%m==0 else 0