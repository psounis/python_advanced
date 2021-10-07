import re

text = "Computer Science is no more about computers " + \
       "than astronomy is about telescope"

print(re.search(r"comp.", text))
print(re.search(r"Sci.", text))

print("="*20)
pattern = re.compile(r"\ba\w*", re.IGNORECASE)
pos = 0
while True:
    m = pattern.search(text, pos)
    if m:
        print(m.group(), m.span())
        pos = m.end() + 1
    else:
        break

