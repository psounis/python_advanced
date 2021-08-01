addtwo = lambda x: x+2
print(addtwo(5))
print(addtwo(addtwo(1)))

# IIFE (Immediately Invoked Function Expression)
y = (lambda x: x*x)(3)
print(y)