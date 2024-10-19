# def roman2Dec(romStr):
#     roman_dict ={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     # Analyze string backwards
#     romanBack = list(romStr)[::-1]
#     value = 0
#     # To keep track of order
#     rightVal = roman_dict[romanBack[0]]
#     for numeral in romanBack:
#         leftVal = roman_dict[numeral]
#         # Check for subtraction
#         if leftVal < rightVal:
#            value -= leftVal
#         else:
#             value += leftVal
#         rightVal = leftVal
#     return value
#
#
# romanStr = input("Enter a Roman Number : ")
# print(roman2Dec(romanStr))

def roman2dec(rom):
 roman_dict ={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
 value=0
 for i in range(len(rom)):
     if i>0 and roman_dict[rom[i]]>roman_dict[rom[i-1]]:
         value+=roman_dict[rom[i]]-2*roman_dict[rom[i-1]]
     else:
         value+=roman_dict[rom[i]]
 return value
rom = input("Enter a Roman Number : ")
print(roman2dec(rom))
