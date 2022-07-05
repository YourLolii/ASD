####REGEX
import re

##s = "Sayaaaa beli baksooo"
##
##cocok = re.findall(r'..a+', s)
##
##print (cocok)

f = open('aaaa.txt', 'r', encoding='latin1')
s = f.read()
f.close()
cocok = re.findall(r'ii\w+',s)
print(cocok)
