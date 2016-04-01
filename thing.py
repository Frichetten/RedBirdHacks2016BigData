import csv
from collections import Counter

def fileIO():
    #Attempt to open file
    try:
        file = open('Crash_Qtr01_2015.csv', 'r+')
    except IOError:
        inp = raw_input("Cannot find file. Create one? (y/n)")
        if inp == 'y':
            print "Created file."
            file = open('data.csv', 'w+')
        else:
            print "Ending."
    return file

reader = csv.reader(fileIO())
data = []
for row in reader:
       data.append(row[2])

n = Counter()
n.update('hanza')
n.update('man')
print Counter(data).most_common()
