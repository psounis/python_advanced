from functools import reduce

students = [
    {
        "name": "Bob",
        "grade": 5,
    },
    {
        "name": "Pat",
        "grade": 7
    },
    {
        "name": "Tom",
        "grade": 2
    }
]



# students that passed
print(reduce(lambda x, y: x+[y["name"]] if y["grade"]>=5 else x, students, []))

# get the entries with just the names of students that passed
print(reduce(lambda x, y: x+[{"name": y["name"]}] if y["grade"]>=5 else x, students, []))

# student with lowest grade
print(reduce(lambda x, y: x if x["grade"] < y["grade"] else y,students, (students[0])))