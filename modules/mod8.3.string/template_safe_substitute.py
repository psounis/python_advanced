from string import Template

template2 = Template("$name makes $salary$$") # $$ escapes $

sub21 = template2.safe_substitute({"name": "Bob", "salary": 1000})
print(sub21)
try:
    sub22 = template2.substitute(name="Bob")
    print(sub22)
except KeyError:
    print("KeyError")
sub23 = template2.safe_substitute({"name": "Bob"})
print(sub23)