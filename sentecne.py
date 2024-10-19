sent=input("enter a sentence")
list=sent.split(" ")
print("this setence hasn",len(list),"words")
dig=up=lw=0
for ch in sent:
    if '0'<=ch<='9':
        dig+=1
    elif 'a'<=ch<='z':
        lw+=1
    elif 'A'<=ch<="Z":
        up+=1
print("it has",dig,"up",up,"low",lw)