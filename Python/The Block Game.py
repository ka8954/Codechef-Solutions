t = int(input())

def isPalindrome(s):
    return s == s[::-1]
    
for i in range(0,t):
    n = input()
    
    if isPalindrome(n):
        print("wins")
    else:
        print("loses")
