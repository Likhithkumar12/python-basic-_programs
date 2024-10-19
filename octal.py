conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                    13: 'D', 14: 'E', 15: 'F'}
def bin2dec(val):
    rev=val[::-1]
    dec=0
    i=0
    for dig in rev:
        dec=dec+int(dig)*2**i
        i+=1
    return dec
def oct2hex(val):



   rev=val[::-1]
   dec=0
   i=0
   for dig in rev:
       dec+=int(dig)*8**i
       i+=1

   print("decimal",dec)
   hex=""
   while dec!=0:
       rem=dec%16
       hex=conversion_table[rem]+hex
       dec=dec//16
   print("hex",hex)
val=input("entera octal number")
oct2hex(val)