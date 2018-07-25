import sys
sys.path.append('..')

from lib.stack import Stack

def base_converter(dec_number, base):
    digits = "0123456789ABCDEF"
    s=Stack()
    while dec_number!=0:
        s.push(digits[dec_number%base])
        dec_number=dec_number//base
        
    string=''
    while not s.isEmpty():
        string=string+s.pop()
    
    return string

print(base_converter(1000,16))  # 回傳 3E8
print(base_converter(700, 12))  # 回傳 4A4
