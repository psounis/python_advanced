from csv import reader, writer

with open("excel.csv", "r") as file:
    csv_reader = reader(file, delimiter=";")
    data = list(csv_reader)

data[1][1] = "Bob,tom"

with open("excel_new2.csv", "w", newline="") as file:
    csv_writer = writer(file, delimiter=",", quotechar="'")
    for row in data:
        csv_writer.writerow(row)

