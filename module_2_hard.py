import random

N = 12
dividers = list()   #[]
ans = str()

for div in range(3, N//2+1):    # 3 4 5 6 7
    if N % div == 0:
        dividers.append(div)
dividers.append(N)

for i in range(1, N//2+1):    # 1 2 3 4 5 6 7
    for div in dividers:
        if i <= div//2 and i != div - i:
            ans += f"{i}{div - i}"
print(ans)




