
def fn(n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return fn(n-1)+fn(n-2)
n=int(input("enter a number"))
if n>0:
    print("fn(",n,")=",fn(n))
else:
    print("invalid")