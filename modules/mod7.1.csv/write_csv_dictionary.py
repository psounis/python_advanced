from csv import DictReader, DictWriter

with open("countries.csv", "r", encoding="utf-8") as file:
    csv_reader = DictReader(file)
    data = list(csv_reader)

with open("countries_new3.csv", "w", encoding="utf-8", newline="") as file:
    csv_writer = DictWriter(file, fieldnames=["Name", "Continent"])
    csv_writer.writeheader()
    for row in data:
        new_row = {"Name": row["Name"],
                   "Continent": row["Continent"]}
        csv_writer.writerow(new_row)
