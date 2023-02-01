t = int(input())

for i in range(0,t):
    x,y = map(int,input().split())
    res = x//2
    if res<y:
        print(res)
    else:
        print(y)
    
