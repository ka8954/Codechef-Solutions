t = int(input())

for i in range(0,t):
    n = int(input())
    val = (2**n)-1
    x=0
    count=0
    while (x>0 or x==0) and (x<val or x==val):
        
        if (x^(x+1)) == ((x+2)^(x+3)):
            count=count+1
            x=x+1
        else:
            x=x+1
    print(count)        
