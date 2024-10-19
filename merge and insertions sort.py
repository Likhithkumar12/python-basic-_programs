import random
def mergesort(list):
    if len(list)>1:
        mid=len(list)//2
        left=list[:mid]
        right=list[mid:]
        mergesort(left)
        mergesort(right)
        i=j=k=0
        while i<len(left)and j<len(right):
            if left[i]<right[j]:
                list[k]=left[i]
                i+=1
            else:
                list[k]=right[j]
                j+=1
            k+=1
        while i <len(left):
            list[k]=left[i]
            i+=1
            k+=1
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
    return list
def insertionsort(list):
    for i in range(1,len(list)):
        key=list[i]
        j=i-1
        while j>=0 and key<list[j]:
            list[j+1]=list[j]
            j-=1
        list[j+1]=key
    return list
list=[]
for i in range(10):
    list.append(random.randint(0,999))
print(insertionsort(list))
