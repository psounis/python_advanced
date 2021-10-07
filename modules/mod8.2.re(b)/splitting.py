import re

text = "Computer Science is no more about computers, " + \
       "than astronomy is about telescope."

print(re.split(r" ", text))
print(re.split(r"\W? \W?", text))
print(re.split(r"\W? +\W?|\W", text))