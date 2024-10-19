
val=input("enter a string")
if val==val[::-1]:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
for i in range(10):
    if val.count(str(i))> 0:
        print(str(i),"appears",val.count(str(i)),"times")