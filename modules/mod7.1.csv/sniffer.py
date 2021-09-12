from csv import reader, Sniffer

with open("countries.csv", "r", encoding="utf-8") as file:
    sniff = Sniffer().sniff(file.read(1024))
    file.seek(0)
    csv_reader = reader(file, dialect=sniff)
    dialect = csv_reader.dialect
    print("delimiter: " + dialect.delimiter)
    print("quotechar: " + dialect.quotechar)
    print("lineterminator: " + dialect.lineterminator)
    data = list(csv_reader)
    print(data)
