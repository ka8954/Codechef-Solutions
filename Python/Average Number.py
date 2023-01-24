t = int(input())

for i in range(0,t):
    
    n,k,v = map(int,input().split())
    l=list(map(int,input().split()))
    res = ((v*(n+k)) - sum(l))
    if (res%k)==0 and res>0:
        print(res//k)
    else:
        print("-1")
