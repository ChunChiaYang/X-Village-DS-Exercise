import sys
sys.path.append('..')

from lib.stack import Stack


def dec_to_bin(dec):
    # Finish the function
    s=Stack()
    while dec!=0:
        s.push(dec%2)
        dec=dec//2
        
    binary=[]
    while not s.isEmpty():
        binary.append(s.pop())
        
    return binary

print(*dec_to_bin(42))   # 回傳 101010
print(*dec_to_bin(100))  # 回傳 1100100
