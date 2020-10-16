class MyIterator:
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        self.n += 1
        return self.n


obj = MyIterator()
it = iter(obj)
print(next(it))
print(next(it))
print(next(it))