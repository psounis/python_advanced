import re


def matches(text, regexp):
    pattern = re.compile(regexp)
    matcher = pattern.fullmatch(text)
    if matcher is None:
        return False
    else:
        return True


print(matches("\\\\", r"\\{2,}"))

print("=" * 10)

text = "Everything about me is a contradiction, " + \
       "and so is everything about everybody else.\n " + \
       "We are made out of oppositions; we live between two poles.\n " + \
       "There's a philistine and an aesthete in all of us, " + \
       "and a murderer and a saint.\n You don't reconcile the poles.\n " + \
       "You just recognize them."

print(re.split(r"\n *", text))
