import re


text = "Computer Science is no more about computers " + \
       "than astronomy is about telescope"

m = re.match(r".* (?P<previous>\w+?) is (?P<next>\w+?) .*", text)
print(m[1], "|", m[2])
print(m["previous"], m["next"])
print(m.groupdict())
print(m.group(), m.group(0))
print(m.group(1), m.group(2), m.group(1, 2))

for i in range(m.lastindex+1):
    print(m.span(i), end=" ")
    print(m.group(i))

