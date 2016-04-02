import csv
from collections import Counter
from matplotlib import pyplot as plt

def fileIO(filename):
    file = open(filename, 'r+')
    return file


#Greet use and ask for report number
rnum = raw_input("Please Enter Accident Report #: ")

flag = False
filename = "Qtr01_Accident.csv"
reader = csv.reader(fileIO(filename))
for row in reader:
    if row[10] == rnum:
        flag = True
        print '\nAccident Data'
        print 'Report No.: ', rnum, " Acc_Date: ",row[12]," Acc_time: "  , row[13]
        print 'County_NO.: ', row[1], ' Weather code: ', row[11]
        print 'Collision Type: ', row[4], '\n'

dict1 = {}
if flag:
    print 'Vehicle Data'
reader = csv.reader(fileIO('Qtr01_Vehicle.csv'))
for row in reader:
    if row[5] == rnum:
        print row[8] , " ", row[10]
        print 'Towed Away?: ', row[12]
        print 'Damage Codes: ', row[25]," ",row[26]," ",row[27]," ",row[28]," ",row[29]
        dict1[row[23]] = row[10]

if flag:
    print '\nPerson Data'
reader = csv.reader(fileIO('Qtr01_Circum_Person.csv'))
for row in reader:
    if row[0] == rnum:
        print 'Contribution Code: ', row[2]

reader = csv.reader(fileIO('Qtr01_Person.csv'))
for row in reader:
    if row[3] == rnum:
        if row[25] != '':
            print dict1[row[25]]
        print 'Sex: ',row[0],' Condition: ',row[1],' Injury code: ',row[2]
        print 'Type ',row[10], ' Fault flag: ',row[16]
        print 'DOB: ',row[20],'\n'
        flag = False

filename = "Qtr02_Accident.csv"
reader = csv.reader(fileIO(filename))
for row in reader:
    if row[10] == rnum:
        flag = True
        print '\nAccident Data'
        print 'Report No.: ', rnum, " Acc_Date: ",row[12]," Acc_time: "  , row[13]
        print 'County_NO.: ', row[1], ' Weather code: ', row[11]
        print 'Collision Type: ', row[4], '\n'

dict2 = {}
if flag:
    print 'Vehicle Data'
reader = csv.reader(fileIO('Qtr02_Vehicle.csv'))
for row in reader:
    if row[5] == rnum:
        print row[8] , " ", row[10]
        print 'Towed Away?: ', row[12]
        print 'Damage Codes: ', row[25]," ",row[26]," ",row[27]," ",row[28]," ",row[29]
        dict2[row[23]] = row[10]

if flag:
    print '\nPerson Data'
reader = csv.reader(fileIO('Qtr02_Circum_Person.csv'))
for row in reader:
    if row[0] == rnum:
        print 'Contribution Code: ', row[2]

reader = csv.reader(fileIO('Qtr02_Person.csv'))
for row in reader:
    if row[3] == rnum:
        if row[25] != '':
            print dict2[row[25]]
        print 'Sex: ',row[0],' Condition: ',row[1],' Injury code: ',row[2]
        print 'Type ',row[10], ' Fault flag: ',row[16]
        print 'DOB: ',row[20],'\n'
        flag = False

filename = "Qtr03_Accident.csv"
reader = csv.reader(fileIO(filename))
for row in reader:
    if row[10] == rnum:
        flag = True
        print '\nAccident Data'
        print 'Report No.: ', rnum, " Acc_Date: ",row[12]," Acc_time: "  , row[13]
        print 'County_NO.: ', row[1], ' Weather code: ', row[11]
        print 'Collision Type: ', row[4], '\n'

dict3 = {}
if flag:
    print 'Vehicle Data'
reader = csv.reader(fileIO('Qtr03_Vehicle.csv'))
for row in reader:
    if row[5] == rnum:
        print row[8] , " ", row[10]
        print 'Towed Away?: ', row[12]
        print 'Damage Codes: ', row[25]," ",row[26]," ",row[27]," ",row[28]," ",row[29]
        dict3[row[23]] = row[10]

if flag:
    print '\nPerson Data'
reader = csv.reader(fileIO('Qtr03_Circum_Person.csv'))
for row in reader:
    if row[0] == rnum:
        print 'Contribution Code: ', row[2]

reader = csv.reader(fileIO('Qtr03_Person.csv'))
for row in reader:
    if row[3] == rnum:
        if row[25] != '':
            print dict3[row[25]]
        print 'Sex: ',row[0],' Condition: ',row[1],' Injury code: ',row[2]
        print 'Type ',row[10], ' Fault flag: ',row[16]
        print 'DOB: ',row[20],'\n'
        flag = False

filename = "Qtr04_Accident.csv"
reader = csv.reader(fileIO(filename))
for row in reader:
    if row[10] == rnum:
        flag = True
        print '\nAccident Data'
        print 'Report No.: ', rnum, " Acc_Date: ",row[12]," Acc_time: "  , row[13]
        print 'County_NO.: ', row[1], ' Weather code: ', row[11]
        print 'Collision Type: ', row[4], '\n'

dict4 = {}
if flag:
    print 'Vehicle Data'
reader = csv.reader(fileIO('Qtr04_Vehicle.csv'))
for row in reader:
    if row[5] == rnum:
        print row[8] , " ", row[10]
        print 'Towed Away?: ', row[12]
        print 'Damage Codes: ', row[25]," ",row[26]," ",row[27]," ",row[28]," ",row[29]
        dict4[row[23]] = row[10]

if flag:
    print '\nPerson Data'
reader = csv.reader(fileIO('Qtr04_Circum_Person.csv'))
for row in reader:
    if row[0] == rnum:
        print 'Contribution Code: ', row[2]

reader = csv.reader(fileIO('Qtr04_Person.csv'))
for row in reader:
    if row[3] == rnum:
        if row[25] != '':
            print dict4[row[25]]
        print 'Sex: ',row[0],' Condition: ',row[1],' Injury code: ',row[2]
        print 'Type ',row[10], ' Fault flag: ',row[16]
        print 'DOB: ',row[20],'\n'
        flag = False
