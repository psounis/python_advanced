import re

text = "Computer Science is no more about computers, " + \
       "than astronomy is about telescope."

print(re.findall(r"\w+", text))
print(re.findall(r"(\w+) about (\w+)", text))
print(re.findall(r"((\w+) about (\w+))", text))

print("="*20)

text = "Everything about me is a contradiction, " + \
       "and so is everything about everybody else.\n " + \
       "We are made out of oppositions; we live between two poles.\n " + \
       "There's a philistine and an aesthete in all of us, " + \
       "and a murderer and a saint.\nYou don't reconcile the poles.\n" + \
       "You just recognize them."

pattern = re.compile(r"^(Y\w+) ([\w']+) (\w+)", re.MULTILINE)
print(pattern.findall(text))
