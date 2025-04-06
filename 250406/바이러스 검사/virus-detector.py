n = int(input())
people = []
people.append(list(map(int,input().split())))
ldr, mbr = map(int,input().split())

result = n

for i in range(n):
    people[0][i] = people[0][i] - ldr
    if people[0][i] > 0
        if(people[0][i]%mbr != 0):
            result += 1
        result += people[0][i] // mbr

print(result)