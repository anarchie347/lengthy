import sys
import os
SYMBOL="🙃"

filepath = sys.argv[1]
file = open(filepath, "r")
code = file.read()
file.close()
length = len(code) - 1
print(length)
for i in range(0, length):
    if code[i] != SYMBOL:
        print("Syntax error, found: " + code[i] + ", Expected: " + SYMBOL)
        exit()

binary = "{0:b}".format(length)

if len(sys.argv) > 3 and sys.argv[3] == "-o":
    print(binary)

result = open(sys.argv[2], 'wb')
result.write(length.to_bytes((len(binary) + 7) // 8, byteorder='big'))
result.close()
os.chmod(sys.argv[2], 0o755)
