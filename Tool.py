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

filename = 'Qtr01_Accident.csv'
reader = csv.reader(fileIO(filename))
Q1counter = -1
for row in reader:
       Q1counter += 1

filename = 'Qtr02_Accident.csv'
reader= csv.reader(fileIO(filename))
Q2counter = -1
for row in reader:
       Q2counter += 1

filename = 'Qtr03_Accident.csv'
reader= csv.reader(fileIO(filename))
Q3counter = -1
for row in reader:
       Q3counter += 1

filename = 'Qtr04_Accident.csv'
reader= csv.reader(fileIO(filename))
Q4counter = -1
for row in reader:
       Q4counter += 1

sum = Q1counter + Q2counter + Q3counter + Q4counter

accidents = ["Q1 Accidents", "Q2 Accidents", "Q3 Accidents", "Q4 Accidents"]
sums = [Q1counter, Q2counter, Q3counter, Q4counter]
xs = [i+0.1 for i, _ in enumerate(accidents)]
plt.bar(xs,sums)

plt.ylabel("Number of Accidents")
plt.title("Number of Accidents Per Quarter")

plt.xticks([i + 0.5 for i, _ in enumerate(accidents)], accidents)

plt.show()
