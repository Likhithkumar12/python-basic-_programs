m1=int(input("enter the first number"))
m2=int(input("enter the second number"))
m3=int(input("enter the second number"))
if m1<=m2 and m1<=m3:
    avg=(m2+m3)/2
elif m2<=m1 and m2<=m3:
    avg=(m1+m3)/2
else:
    avg=(m1+m2)/2
print(avg)