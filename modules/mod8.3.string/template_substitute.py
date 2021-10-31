from string import Template

template1 = Template("$name lives in $place")

sub11 = template1.substitute({"name": "Bob", "place": "Athens"})
print(sub11)
sub12 = template1.substitute(name="Bob", place="Athens")
print(sub12)
sub13 = template1.substitute({"name": "Bob"}, place="Athens")
print(sub13)


