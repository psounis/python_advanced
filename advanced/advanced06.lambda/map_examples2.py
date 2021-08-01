print(list(map(lambda x,y: x+y, [1,2,3], [4,5,6])))

print(dict(list(map(lambda x,y:
                    (x,y), [1,2,3],
                    ["one", "two", "three"]))))

print(list(map(lambda x,y,z:
               {"id": x, "name": y, "grade": z},
                    (i for i in range(1000)),
                    ["Bob", "Tom", "Pat"],
                    [5,8,2])))


