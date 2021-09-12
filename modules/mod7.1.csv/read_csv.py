from csv import reader

with open("countries.csv", "r", encoding="utf-8") as file:
    csv_reader = reader(file)
    print(type(csv_reader))
    for row in csv_reader:
        print(row)