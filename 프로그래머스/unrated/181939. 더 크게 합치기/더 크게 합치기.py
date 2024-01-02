def solution(a, b):
    x = int(str(a)+str(b))
    y = int(str(b)+str(a))
    if(x>y):
        return x
    else:
        return y