import re


text = "Computer Science is no more about computers " + \
       "than astronomy is about telescope"

m = re.match(r".* (\w+?) is (\w+?) .*", text)
print(m.group(0) + "|" + m.group(1) + "|" + m.group(2))
print(m[0] + "|" + m[1] + "|" + m[2])
