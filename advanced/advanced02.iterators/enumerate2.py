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


for index, iter_value in enumerate(MyIterator(),100):
    print(index, iter_value)
