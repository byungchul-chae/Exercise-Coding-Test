def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        a = arr[s:e+1]
        ans = [i for i in a if i > k]
        if(len(ans)==0):
            answer += [-1]
        else:
            answer += [min(ans)]
    return answer