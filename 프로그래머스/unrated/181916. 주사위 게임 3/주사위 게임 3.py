def solution(a, b, c, d):
    answer = 0
    arr = [a,b,c,d]
    s = list(set(arr))
    l = len(s)
    c = []
    for i in range(l):
        c.append(arr.count(s[i]))
    
    if(l == 1):
        answer = 1111 * s[0]
    elif(l == 2):
        if(c[0] == 2):
            answer = (s[0]+s[1])*abs(s[0]-s[1])
        else:
            for idx, i in enumerate(c):
                if(i == 3):
                    answer = (10*s[idx]+s[idx-1])**2
    elif(l==3):
        for idx, i in enumerate(c):
            if(i == 2):
                answer = s[idx-1] * s[idx-2]
    elif(l==4):
        answer = min(s)
    return answer