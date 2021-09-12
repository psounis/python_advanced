from csv import DictReader

with open("countries.csv", "r", encoding="utf-8") as file:
    csv_reader = DictReader(file)
    data = list(csv_reader)
    print(data)

print("="*25)
row = data[0]
print(row)
print(row["Name"], row["Continent"])
