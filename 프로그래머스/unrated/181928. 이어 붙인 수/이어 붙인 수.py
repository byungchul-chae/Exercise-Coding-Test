def solution(num_list):
    o = ''
    e = ''
    for i in num_list:
        if(i%2):
            e = e + str(i)
        else:
            o = o + str(i)
    return int(e)+int(o)