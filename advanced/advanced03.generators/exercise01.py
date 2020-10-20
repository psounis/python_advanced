class MyIterator:
    def __iter__(self):
        self.i = 9
        return self

    def __next__(self):
        self.i += 1
        if self.i <= 20:
            return self.i ** 2
        else:
            raise StopIteration


for i in MyIterator():
    print(i)


def MyGenerator():
    for i in range(10,21):
        yield i*i

for i in MyGenerator():
    print(i)


g = (i*i for i in range(10,21))

for i in g:
    print(i)
