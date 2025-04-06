n = int(input())
work = [list(map(int, input().split())) for _ in range(n)]

max_result = 0  # 최대 수익

def backtrack(day, total_income):
    global max_result

    if day >= n:
        max_result = max(max_result, total_income)
        return

    # 1. 일할 수 있는 경우: 오늘부터 period만큼 일할 수 있는가?
    period, income = work[day]
    if day + period <= n:
        backtrack(day + period, total_income + income)

    # 2. 일을 안하고 다음 날로 넘어가는 경우
    backtrack(day + 1, total_income)

backtrack(0, 0)
print(max_result)