import re
f=open('New Text Document.txt','r')

print(re.findall(r'([\w]+)+z',f.read()))
