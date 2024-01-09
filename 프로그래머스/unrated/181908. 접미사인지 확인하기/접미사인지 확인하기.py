def solution(my_string, is_suffix):
    answer = 0
    arr = []
    for i in range(len(my_string)):
        arr.append(my_string[-i:])
    return 1 if is_suffix in arr else 0 
    # return int(my_string.endswith(is_suffix))