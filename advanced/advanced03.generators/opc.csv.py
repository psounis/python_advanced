# source: https://www.dataquest.io/blog/python-generators-tutorial/
data = "sample.csv"
lines = (line for line in open(data, encoding="ISO-8859-1"))
for line in lines:
    cells = line.split(",")
    for c in cells:
        print(c.strip(), end="\t")
    print("")