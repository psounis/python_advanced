import re

with open("pies.html", encoding="utf-8") as f:
    text = f.read()
    print(text)


res = re.findall(r"\bπίτες\b", text)
print(res)

res2 = re.findall(r"(\b\w*?)\Bπιτες\b", text)
print(res2)

res3 = re.findall(r"\ba.*?\b", text)
print(res3)

