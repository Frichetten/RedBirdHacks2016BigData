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

qtr1 = []
dict1 = {}
filename = "Qtr01_Circum_Person.csv"
reader = csv.reader(fileIO(filename))
for row in reader:
    data.append(row[2])

#print Counter(qtr1).most_common()

qtr2 = []
filename = "Qtr02_Circum_Person.csv"
reader = csv.reader(fileIO(filename))
for row in reader:
    data.append(row[2])

#print Counter(qtr2).most_common()

qtr3 = []
filename = "Qtr03_Circum_Person.csv"
reader = csv.reader(fileIO(filename))
for row in reader:
    data.append(row[2])

#print Counter(qtr3).most_common()

qtr4 = []
filename = "Qtr04_Circum_Person.csv"
reader = csv.reader(fileIO(filename))
for row in reader:
    data.append(row[2])

#print Counter(qtr4).most_common()
    
reasons = ['Fail. Pay Attn.','Speeding','Fail. Yield r.o.w','Following Too Closely','Alcohol','Ran off road','Imp. Lane Change','Asleep At Wheel']
values = [33996,11601,10426,8910,4488,3036,2938,2116]
xs = [i + 0.1 for i, _ in enumerate(reasons)]
plt.bar(xs, values)
plt.ylabel("# of Accidents")
plt.title("# of Accidents Attributed to Reasons")
plt.xticks([i + 0.5 for i, _ in enumerate(reasons)], reasons)
plt.show()
