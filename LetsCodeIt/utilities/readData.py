import csv


def getReadData(fileName):
    rows = []
    dataFile = open(fileName, 'r')
    reader = csv.reader(dataFile)
    next(reader)
    for row in reader:
        rows.append(row)
    return rows
