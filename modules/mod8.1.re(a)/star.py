import re


def matches(text, regexp):
    pattern = re.compile(regexp)
    matcher = pattern.fullmatch(text)
    if matcher is None:
        return False
    else:
        return True


print(matches("", r"a*"))
print(matches("a", r"a*"))
print(matches("aa", r"a*"))
print(matches("aab", r"a*"))

print("=" * 10)
print(matches("Niger", r".*er"))
print(matches("Niger", r".*em"))
print(matches("Mexico", r"Me.*"))
print(matches("Nexico", r"Me.*"))
print(matches("Nicaragua", r".*ar.*"))
print(matches("Nicaaagua", r".*ar.*"))
print(matches("Morocco", r"M.*ro.*o"))

print("=" * 10)
print(matches("Mexico", r"(..)*"))
print(matches("USA", r"(..)*"))
print(matches("Burundi", r"B(u.)*di"))



