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


obj = MyIterator()
it = iter(obj)
for i in it:
    print(i)

for i in obj:
    print(i)