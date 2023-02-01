t = int(input())

for i in range(0,t):
    m,n,k = map(int,input().split())
    
    if m-(n*k)>0:
        print("YES")
    else:
        print("NO")
