import csv
from collections import Counter
from matplotlib import pyplot as plt

def fileIO(filename):
    #Attempt to open file
    try:
        file = open(filename, 'r+')
    except IOError:
        inp = raw_input("Cannot find file. Create one? (y/n)")
        if inp == 'y':
            print "Created file."
            file = open('data.csv', 'w+')
        else:
            print "Ending."
    return file

data = []
ao = 0

qtr1 = []
dict1 = {}
filename = "Qtr01_Circum_Person.csv"
reader = csv.reader(fileIO(filename))
for bag in reader:
    dict1[bag[0]] = bag[2]

filename = "Qtr01_Person.csv"
reader = csv.reader(fileIO(filename))
for row in reader:
    if row[10] == 'D':
        qtr1.append(row[0])

print Counter(qtr1).most_common()

qtr2 = []
dict2 = {}
filename = "Qtr02_Circum_Person.csv"
reader = csv.reader(fileIO(filename))
for bag in reader:
    dict2[bag[0]] = bag[2]

filename = "Qtr02_Person.csv"
reader = csv.reader(fileIO(filename))
for row in reader:
    if row[10] == 'D':
        qtr2.append(row[0])

print Counter(qtr2).most_common()

qtr3 = []
dict3 = {}
filename = "Qtr03_Circum_Person.csv"
reader = csv.reader(fileIO(filename))
for bag in reader:
    dict3[bag[0]] = bag[2]

filename = "Qtr03_Person.csv"
reader = csv.reader(fileIO(filename))
for row in reader:
    if row[10] == 'D':
        qtr3.append(row[0])

print Counter(qtr3).most_common()

qtr4 = []
dict4 = {}
filename = "Qtr04_Circum_Person.csv"
reader = csv.reader(fileIO(filename))
for bag in reader:
    dict4[bag[0]] = bag[2]

filename = "Qtr04_Person.csv"
reader = csv.reader(fileIO(filename))
for row in reader:
    if row[10] == 'D':
        qtr4.append(row[0])

print Counter(qtr4).most_common()

genders = ['Male','Female']
values = [328, 144]
xs = [i + 0.1 for i, _ in enumerate(genders)]
plt.bar(xs, values)
plt.ylabel('Number of Fatalities')
plt.title('Traffic Fatalities by Gender')
plt.xticks([i + 0.5 for i, _ in enumerate(genders)],genders)
plt.show()
