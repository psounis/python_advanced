# source: https://www.journaldev.com/14620/python-iterator

class fibo:
    def __init__(self):
        # default constructor
        self.prev = 0
        self.cur = 1
        self.n = 1

    def __iter__(self):  # define the iter() function
        return self

    def __next__(self):  # define the next() function
        if self.n < 10:  # Limit to 10
            # calculate fibonacci
            result = self.prev + self.cur
            self.prev = self.cur
            self.cur = result
            self.n += 1
            return result
        else:
            raise StopIteration  # raise exception

# init the iterator
iterator = iter(fibo())
# Try to print infinite time until it gets an exception
while True:
    # print the value of next fibonacci up to 10th fibonacci
    try:
        print(next(iterator))
    except StopIteration:
        print('First 9 fibonacci numbers have been printed already.')
        break  # break the loop