def solution(ineq, eq, n, m):
    if(ineq=='>' and eq=='='):
        return 1 if n>=m else 0
    elif(ineq=="<" and eq=="="):
        return 1 if n<=m else 0
    elif(ineq==">" and eq=="!"):
        return 1 if n>m else 0
    elif(ineq=="<" and eq=="!"):
        return 1 if n<m else 0
    #return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))
