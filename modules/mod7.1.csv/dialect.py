from csv import reader, writer

with open("excel.csv", "r") as file:
    csv_reader = reader(file, delimiter=";")
    dialect = csv_reader.dialect
    print("delimiter: " + dialect.delimiter)
    print("quotechar: " + dialect.quotechar)
    print("lineterminator: " + dialect.lineterminator)

