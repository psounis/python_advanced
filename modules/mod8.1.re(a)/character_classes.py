import re


def matches(text, regexp):
    pattern = re.compile(regexp)
    matcher = pattern.fullmatch(text)
    if matcher is None:
        return False
    else:
        return True


print(matches("abb", r"[abc]*"))
print(matches("abZ", r"[a-z]*"))
print(matches("abdm", r"[a-dm-p]*"))
print(matches("ffxm", r"[^a-d]*"))

print("=" * 10)

print(matches("psounis21@gmail.com",
              r"[a-zA-Z1-9]{8,12}@gmail.com"))
print(matches("1.psounis@gmail.com",
              r"[a-zA-Z1-9]{8,12}@gmail.com"))
print(matches("psounis-21@gmail.com",
              r"[a-zA-Z0-9_-]+@[a-zA-Z]+\.com"))
