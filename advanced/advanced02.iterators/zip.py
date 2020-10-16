class MyIterator:
    def __init__(self,n):
        self.n = n

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i<=10:
            return self.n + self.i
        else:
            raise StopIteration


a = MyIterator(10)
b = MyIterator(20)
c = MyIterator(30)


for x,y,z in zip(a,b,c):
    print(x,y,z)
