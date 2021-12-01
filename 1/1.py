import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    data = []
    for row in reader:
        if len(row) > 0:
            data.append(int(row[0]))

# First star
first = map(lambda i, j: i < j, data[0:-1], data[1:])
print(sum(list(first)))

#Second star
first = map(lambda i, j, k, l: i+j+k < j+k+l, data[0:-3], data[1:-2], data[2:-1], data[3:])
print(sum(list(first)))


