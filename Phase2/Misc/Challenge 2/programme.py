from pwn import *
import base64 as b64
import codecs


my_dict = {
    'A': '@!@@!',
    'B': '@!@@@',
    'C': '@@!!!',
    'D': '@@!!@',
    'E': '!!!!!',
    'F': '!!!!@',
    'G': '!!!@!',
    'H': '!!!@@',
    'I': '!!@!!',
    'J': '!!@!@',
    'K': '!!@@!',
    'L': '!!@@@',
    'M': '!@!!!',
    'N': '!@!!@',
    'O': '!@!@!',
    'P': '!@!@@',
    'Q': '!@@!!',
    'R': '!@@!@',
    'S': '!@@@!',   
    'T': '!@@@@',
    'U': '@!!!!',
    'V': '@!!!@',
    'W': '@!!@!',
    'X': '@!!@@',
    'Y': '@!@!!',
    'Z': '@!@!@'
}

def value(dictionary, search_value):
    for key, value in dictionary.items():
        if value == search_value:
            return key
    return None
def base64_decode(encoded_text):
    return base64.b64decode(encoded_text.encode('utf-8')).decode('utf-8', errors='ignore')
def rot_13(text):
    return text.translate(str.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"))
def hex(hex_string):
    if hex_string.startswith('0x'):
        hex_string = hex_string[2:]
    decimal_value = int(hex_string, 16)
    ascii_character = chr(decimal_value)
    return ascii_character
def octal(octal_string):
    decimal_value = int(octal_string[2:], 8)
    ascii_character = chr(decimal_value)
    return ascii_character

def decimal(decimal_string):
    decimal_value = int(decimal_string)
    ascii_character = chr(decimal_value)
    return ascii_character
def case(word, shift):
    result = ""
    for char in word:
        ascii_offset = ord('A') if char.isupper() else ord('a')
        result += (chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset))
        a=str(result)
    return a
def caes(word, shift):
    result = ""
    for char in word:
        ascii_offset = ord('A') if char.isupper() else ord('a')
        result += (chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset))
    return result

io=process('./script')


io.recvline()
for _ in range(10):
    a=io.recvline()
    print(a)
    b=a.decode('utf-8')
    c=b.split()
    z=c[2]
    if(z=='rot_13'):
        ch=''
        for i in range(5,len(c)):
            a=rot_13(c[i])
            ch+=a
        x=ch.encode('utf')
        io.sendline(x)
    elif(z=='base64'):
        ch=''
        for i in range(5,len(c)):
            a=base64_decode(c[i])
            ch+=a
        x=ch.encode('utf')
        io.sendline(x)
    elif(z=='hex'):
        ch=''
        for i in range(5,len(c)):
            a=hex(c[i])
            ch+=a
        x=ch.encode('utf')
        io.sendline(x)
    elif(z=='octal'):
        ch=''
        for i in range(5,len(c)):
            a=octal(c[i])
            ch+=a
        x=ch.encode('utf')
        io.sendline(x)
    elif(z=='decimal'):
        ch=''
        for i in range(5,len(c)):
            a=decimal(c[i])
            ch+=a
        x=ch.encode('utf')
        io.sendline(x)
    print(x)
print(io.recvline())
print(io.recvline())
print(io.recvline())
for i in range(10):
    a=io.recvline()
    print(a)
    b=a.decode('utf-8')
    c=b.split()
    z=c[3]
    x=int(c[6])
    m=case(z,x)
    n=m.encode('utf')
   # print(n)
    io.sendline(n)
print(io.recvline())
print(io.recvline())
print(io.recvline())
print(io.recvline())
print(io.recvline())
print(io.recvline())
p="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
o=p.encode('utf')
print(o)
io.sendline(o)
print(io.recvline())
print(io.recvline())
print(io.recvline())
print(io.recvline())
print(io.recvline())
for _ in range(10):
    a=io.recvline()
    print(a)
    b=a.decode('utf-8')
    c=b.split()
    ch=''
    print(c)
    for i in range(2,len(c)):
        z=value(my_dict,c[i])
        ch+=z
        x=ch.encode('utf')
    io.sendline(x)
    print(x)

io.interactive()