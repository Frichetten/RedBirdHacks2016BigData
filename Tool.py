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
filename = "Qtr01_Vehicle.csv"
reader = csv.reader(fileIO(filename))
qtr1 = []
for row in reader:
        data.append(row[10])

#print Counter(qtr1).most_common()

qtr2 = []
filename = "Qtr02_Vehicle.csv"
reader = csv.reader(fileIO(filename))
for row in reader:
        data.append(row[10])

#print Counter(qtr2).most_common()

qtr3 = []
filename = "Qtr03_Vehicle.csv"
reader = csv.reader(fileIO(filename))
for row in reader:
        data.append(row[10])

#print Counter(qtr3).most_common()

qtr4 = []
filename = "Qtr04_Vehicle.csv"
reader = csv.reader(fileIO(filename))
for row in reader:
        data.append(row[10])

#print Counter(qtr4).most_common()
    
d = ['Accord','Camry','Civic','Altima','Corolla','Impala']
values = [6773, 5365, 4739, 4002, 3869, 2310]
xs = [i + 0.1 for i, _ in enumerate(d)]
plt.bar(xs,values)
plt.xticks([i + 0.5 for i, _ in enumerate(d)],d)
#plt.plot(x, values, color='blue', marker='o', linestyle='solid')
plt.title("Car Models Most Involved In Accidents")
plt.ylabel("Number of Crashes")
plt.show()
