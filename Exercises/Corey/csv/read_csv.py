import csv

with open("names.csv", mode="r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        with open("new_names.csv", mode="a") as csv_write:
            print(line)
            csv_writer = csv.writer(csv_write)
            csv_writer.writerow(line)
