def is_even(x):
    return x%2 == 0

my_list = [1,2,3,4,5]
print(list(filter(is_even, my_list)))
print([x for x in my_list if x%2==0])
print([x for x in my_list if is_even(x)])
print([x for x in my_list if (lambda x: x%2==0)(x)])

