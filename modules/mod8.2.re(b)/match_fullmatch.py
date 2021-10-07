import re

text = "Computer Science is no more about computers " + \
       "than astronomy is about telescope"

print(re.match(r"Comp.", text))
print(re.match(r"Sci.", text))
print(re.compile(r"Sci.").match(text, 9))

print(re.fullmatch(r"Comp.*", text))
print(re.compile(r"Sci\w+").fullmatch(text, 9, 14))
