import re
def isphonenumber(numstr):
    if len(numstr)!=12:
        return False
    for i in range(len(numstr)):
        if i==3 or i==7:
            if numstr[i]!="-":
                return False
        else:
            if numstr[i].isdigit()==False:
                return False
    return True
# def isphonenumber(numStr):
#     if len(numStr) != 12:
#         return False
#     for i in range(len(numStr)):
#         if i==3 or i==7:
#             if numStr[i] != "-":
#                 return False
#         else:
#             if numStr[i].isdigit() == False:
#                 return False
#     return True
def chkphonenumber(numstr):
    ph=re.compile(r'^\d{3}-\d{3}-\d{3}$')
    if ph.match(numstr):
        return True
    else:
        return False
ph_num = input("Enter a phone number : ")
print("Without using Regular Expression")
if isphonenumber(ph_num):
    print("Valid phone number")
else:
    print("Invalid phone number")

print("Using Regular Expression")
if chkphonenumber(ph_num):
    print("Valid phone number")
else:
    print("Invalid phone number")