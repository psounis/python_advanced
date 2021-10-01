import re


def matches(text, regexp):
    pattern = re.compile(regexp)
    matcher = pattern.fullmatch(text)
    if matcher is None:
        return False
    else:
        return True


text = "Computer Science is no more about computers " + \
       "than astronomy is about telescope"

print(re.findall(r"Sci.*? |ast.*? ", text))
