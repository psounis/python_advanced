from csv import reader, writer

with open("countries.csv", "r", encoding="utf-8") as fread, \
        open("countries_new.csv", "w", encoding="utf-8", newline="") as fwrite:
    csv_reader = reader(fread)
    csv_writer = writer(fwrite)
    for line in csv_reader:
        newline = line[:3]+[line[14]]
        csv_writer.writerow(newline)

