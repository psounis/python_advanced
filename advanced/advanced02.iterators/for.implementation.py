iter_obj = iter([1,2,3])
while True:
    try:
        element = next(iter_obj)
        #.. do something with element
    except StopIteration:
        break
