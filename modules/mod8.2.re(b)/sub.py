import re

text = "Men occasionally stumble over the truth, but most of them " \
       "pick themselves up and hurry off as if nothing had happened."

res = re.sub(r"the\w*", "---", text)
print(res)

with open("pies.html", "r", encoding="utf-8") as f:
    text = f.read()
    s = re.sub(r"<ul>", "<ol>", text, 0, re.MULTILINE)
    s2 = re.sub(r"</ul>", "</ol>", s, 0, re.MULTILINE)
with open("pies2.html", "w", encoding="utf-8") as f:
    f.write(s2)