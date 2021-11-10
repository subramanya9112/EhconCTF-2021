import binascii
import re

with open("ocean.txt", "r") as txt_file:
    line = txt_file.readline()

n = int('0b' + "".join(line.split('!')), 2)
text = binascii.unhexlify('%x' % n).decode('utf-8')

r1 = re.findall(r"EHACON{\w+}", text)
if len(r1) >= 1:
    print(r1[0])
