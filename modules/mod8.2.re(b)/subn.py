import re

text = "Men occasionally stumble over the truth, but most of them " \
       "pick themselves up and hurry off as if nothing had happened."


def replace(match_object):
    length = len(match_object.group(0))
    return "-" * length


res = re.subn(r"the\w*", replace, text)
print(res)
