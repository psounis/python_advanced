import re


def matches(text, regexp):
    pattern = re.compile(regexp)
    matcher = pattern.fullmatch(text)
    if matcher is None:
        return False
    else:
        return True


print(matches("a+aa", r"a+aa"))
print(matches("a+aa", r"a\+aa"))
print(matches("a+aa", "a\\+aa"))

print("=" * 10)

text = "Everything about me is a contradiction, " + \
       "and so is everything about everybody else. " + \
       "We are made out of oppositions; we live between two poles. " + \
       "There's a philistine and an aesthete in all of us, " + \
       "and a murderer and a saint. You don't reconcile the poles. " + \
       "You just recognize them."

print(re.split(r"\. *", text))
