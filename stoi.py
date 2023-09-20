# Convert the string "123" into 123, without using the built-in`int()`
# 1. loop through each digit
# 2. find the digit in range object of range(10)
# 3. once the number is found add it to your value
# 4. Multiply each iteration by 10 (start with 0)

def atoi(inputStr):
  outputNum = 0
  for char in inputStr:
    for i in range(10):
      if str(i) == char:
        outputNum = outputNum * 10 + i
  return outputNum

x =input("enter a string")
y = atoi(x)
print(y)