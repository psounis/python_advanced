from array import array

a = array('i', [1, 2, 3])
a.fromlist([4,5,6])
print(a)

a = array('d', [1, 2, 3])
a.fromlist([4,5,6])
print(a)

# deprecated
a = array('u', "abc")
a.fromunicode("αβγ")
print(a)