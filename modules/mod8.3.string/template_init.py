from string import Template

template1 = Template("$name lives in $place")
template2 = Template("$name makes $salary $$") # $$ escapes $

