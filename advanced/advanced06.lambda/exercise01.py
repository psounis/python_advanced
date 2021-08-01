print([x for x in ["aba","anna","baba","aa","baa"] if x == x[::-1]])

print(list(filter(lambda x: x==x[::-1], ["aba","anna","baba","aa","baa"])))
