import os
import csv
import math
counter=0
max_total=0
Candidates=[]
Total=[]
csv_path="election_data.csv"
with open(csv_path,newline='')as csv_variable:
    splitdata=csv.reader(csv_variable,delimiter=',')
    headerrow=next(splitdata)   
    for row in splitdata:
        counter+=1
        if row[2] not in Candidates:
            Candidates.append(row[2])
            Total.append(1)
        else:
            pointer=Candidates.index(row[2])
            Total[pointer]+=1
    for t in Total:
        if t > max_total:
            p=Total.index(t)
            winner=Candidates[p]
        max_total=t
print("Election Results")
print("..................................")
print("Total votes:"+str(counter))
print(".................................")
for name in Candidates:
    print(name+" : "+str(round((Total[Candidates.index(name)]*100.0/counter), 2))+"% ("+str(Total[Candidates.index(name)])+")")
print(".................................")
print("Winner : "+winner)
print(".................................")




