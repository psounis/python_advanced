import re


def matches(text, regexp):
    pattern = re.compile(regexp)
    matcher = pattern.fullmatch(text)
    if matcher is None:
        return False
    else:
        return True


regexp = r"[0-2][0-3]:[0-5]\d"
print(matches("01:49", regexp))
print(matches("11:01", regexp))
print(matches("25:11", regexp))

print("=" * 10)
regexp = r"[0-2][0-3]:[0-5]\d:[0-5]\d(.\d{1,4})?"
print(matches("01:49:12", regexp))
print(matches("11:01:11.11", regexp))
print(matches("22:11:23.11213", regexp))
