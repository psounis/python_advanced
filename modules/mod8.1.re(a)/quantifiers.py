import re


def matches(text, regexp):
    pattern = re.compile(regexp)
    matcher = pattern.fullmatch(text)
    if matcher is None:
        return False
    else:
        return True


print(matches("abb", r"ab+"))
print(matches("abb", r"ab{3,}"))
print(matches("abab", r"(ab){2}"))
print(matches("abab", r"(ab+){2}"))

print("=" * 10)

print(matches("aaaa", r"aa(aa)?"))
print(matches("aaaa", r"(..)+"))
print(matches("aaaa", r".(..)*"))

