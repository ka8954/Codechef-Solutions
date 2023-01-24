t = int(input())

for i in range(0,t):
    
    n = int(input())
    res = list(map(int,input().split()))
    count = 0
    res.sort()
    for i in range(len(res)-1,-1,-2):
        count+=res[i]
    print(count)
    
