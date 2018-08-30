import csv

def read_csv_function(filename, delimiter_character):
    file = open(filename)
    reader = csv.reader(file, delimiter=delimiter_character)

    rownnum = 0
    a = []
    for row in reader:
        a.append(row)
        rownnum += 1
    file.close()

    return a