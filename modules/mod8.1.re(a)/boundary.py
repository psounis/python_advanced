import re

with open("pies.html", encoding="utf-8") as f:
    text = f.read()
    print(text)


res = re.findall(r"^\s*?<(.+?)>", text, re.MULTILINE)
print(res)

res2 = re.findall(r"^\s*?<(.+?)>.*<(/.+?)>$", text, re.MULTILINE)
print(res2)

