print("|{:b}|".format(4))
print("|{:x}|".format(1000))
print("|{:<6.2f}|".format(1))
print("|{:>-10_.4f}|".format(5432.12))
print("|{:.2%}|".format(.3015))
print("|{1:_^-100_.2f}|{0}|".format(1000.1234, 2000.2468))

d = {"a": 5, "b": 10.123}
print("|{d[a]:_^-100_.2f}|{d[b]}|".format(d=d))