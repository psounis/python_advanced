import re


text = "Computer Science is no more about computers " + \
       "than astronomy is about telescope"

m = re.match(r".* (?P<previous>\w+?) is (?P<next>\w+?) .*", text)
print(m["previous"], m["next"])

