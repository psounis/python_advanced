import re


def matches(text, regexp):
    pattern = re.compile(regexp)
    matcher = pattern.fullmatch(text)
    if matcher is None:
        return False
    else:
        return True


with open("pies.html", encoding="utf-8") as f:
    text = f.read()


pattern = re.compile("A.*A", re.IGNORECASE)
res = matches("abba", pattern)
print(res)

res2 = re.findall(r"""
        ^\s*?   # start with some whitespace
        <(.+?)> # extract the first tag you find
        """, text, re.MULTILINE | re.VERBOSE)
print(res2)


