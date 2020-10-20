from random import randrange

def f():
    cnt=0
    for rounds in range(10):
        ret = yield cnt
        if ret is None:
            cnt+=1
        else:
            cnt+=1+ret


it = f()
for it_val in it:
    print(it_val)
    if randrange(2)==0:
        val = it.send(100)
        print(val)