class MyIterator:
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        self.n += 1
        if self.n<=10:
            return self.n
        else:
            raise StopIteration

it = iter(MyIterator())
print(list(it))
print(tuple(it))
print(set(it))
print(frozenset(it))
print(dict(enumerate(it)))