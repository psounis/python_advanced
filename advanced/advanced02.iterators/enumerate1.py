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


print(enumerate(MyIterator()))
print(list(enumerate(MyIterator())))
print(list(enumerate(MyIterator(),100)))
