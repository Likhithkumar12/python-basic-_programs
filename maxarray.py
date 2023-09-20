#program to find the maximum element of an array without using built in fn
def maxindex(arr):
  max= 0
  for i in range(1, len(arr)):
    if arr[max] < arr[i]:
      max = i
  return max

arr = []
n=int(input(("enter the number of elements of array:")))
for i in range(n):
    ele=int(input("enter number"))
    arr.append(ele)


res = maxindex(arr)
print("maximum element is", arr[res],"at index:", res)