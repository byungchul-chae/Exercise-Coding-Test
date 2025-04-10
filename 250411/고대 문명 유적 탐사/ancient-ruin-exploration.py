K, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(5)]
num = list(map(int, input().split()))
ans = []


# 우선순위
# 회전수, 열, 행
def rotate(arr, si, sj):
    new_arr = [row[:] for row in arr]
    for i in range(3):
        for j in range(3):
            new_arr[si + i][sj + j] = arr[si + 3 - (j + 1)][sj + i]
    return new_arr


from collections import deque


def bfs(arr, v, si, sj):
    umul = []
    q = deque()
    q.append((si, sj))
    v[si][sj] = True
    cnt = 1
    while q:
        si, sj = q.popleft()
        umul.append((si, sj))

        for di, dj in (-1, 0), (1, 0), (0, -1), (0, 1):
            ni = si + di
            nj = sj + dj
            if (0 <= ni < 5 and 0 <= nj < 5 and arr[ni][nj] == arr[si][sj] and v[ni][nj] == False):
                q.append((ni, nj))
                v[ni][nj] = True
                cnt += 1

    if cnt >= 3:
        for i, j in umul:
            arr[i][j] = 0
        return cnt
    else:
        return 0


for _ in range(K):
    max_num = 0
    # [1] 탐사진행
    for rot in range(1, 4):  # 0,1,2(90,180,270)
        for r in range(3):
            for c in range(3):
                new_arr = [x[:] for x in arr]
                for _ in range(rot):  # 회전하고
                    new_arr = rotate(new_arr, r, c)

                # 유물 1차 획득
                cnt = 0
                v = [[False] * 5 for _ in range(5)]
                for i in range(5):
                    for j in range(5):
                        if v[i][j] == False:
                            n = bfs(new_arr, v, i, j)
                            cnt += n
                if cnt > max_num:
                    max_num = cnt
                    max_arr = [r[:] for r in new_arr]
                # 최대 유물 개수 찾기 max_num update
                # 배열 저장 max_arr = new_arr
    if max_num == 0:
        break

    # [2] 연쇄획득
    # max_배열에서 새로 채우고 다시 bfs
    while True:
        round_cnt = 0
        for j in range(5):
            for i in range(4, -1, -1):
                if max_arr[i][j] == 0:
                    max_arr[i][j] = num.pop(0)

        v = [[False] * 5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                if not v[i][j]:
                    round_cnt += bfs(max_arr, v, i, j)

        max_num += round_cnt
        if round_cnt == 0:
            break
    arr = [row[:] for row in max_arr]
    ans.append(max_num)

print(' '.join(map(str, ans)))