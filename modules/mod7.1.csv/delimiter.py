from csv import reader, writer

with open("excel.csv", "r") as file:
    csv_reader = reader(file, delimiter=";")
    data = list(csv_reader)

with open("excel_new.csv", "w", newline="") as file:
    csv_writer = writer(file, delimiter=",")
    for row in data:
        csv_writer.writerow(row)

