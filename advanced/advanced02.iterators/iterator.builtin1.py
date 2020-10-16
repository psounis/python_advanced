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


print(list(MyIterator()))
print(f"min={min(MyIterator())}")
print(f"max={max(MyIterator())}")
print(f"sum={sum(MyIterator())}")
print(f"all={all(MyIterator())}")
print(f"any={any(MyIterator())}")