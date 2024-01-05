def solution(code):
    ret = ''
    mode = 0
    for idx, i in enumerate(code):
        if(mode):
            if(i=='1'):
                mode = 0
            else:
                if(idx%2):
                    ret = ret + i
        else:
            if(i=='1'):
                mode = 1
            else:
                if(idx%2==0):
                    ret = ret + i
    if(len(ret)==0):
        return 'EMPTY'
    return ret

    #return "".join(code.split("1"))[::2] or "EMPTY" ....?