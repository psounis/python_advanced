import re


def matches(text, regexp):
    pattern = re.compile(regexp)
    matcher = pattern.fullmatch(text)
    if matcher is None:
        return False
    else:
        return True


text = "Men occasionally stumble over the truth, but most of them " \
       "pick themselves up and hurry off as if nothing had happened."

print(re.findall(r" o.* ", text))
print(re.findall(r" o.*? ", text))

