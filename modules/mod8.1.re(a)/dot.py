import re


def matches(text, regexp):
    pattern = re.compile(regexp)
    matcher = pattern.fullmatch(text)
    if matcher is None:
        return False
    else:
        return True


r = r"a.b."
print(matches("abba", r))
print(matches("baba", r))
print(matches("abbaa", r))
print(matches("acbz", r))
print(matches("aaabba", r))

print("=" * 20)
print(matches("abc", r"..."))
print(matches("abcde", r"..c.."))
print(matches("aa\nbb", r".."))
print(matches("\n\n", r".."))

