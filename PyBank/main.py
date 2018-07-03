import os
import csv
import math
counter=0
total=0
pointer=0
add=0
grincrease=0
grdecrease=0
csvpath="budget_data.csv"
with open(csvpath,newline='') as csv_variable:
    splitdata=csv.reader(csv_variable,delimiter=',')  
    headerrow=next(splitdata)
    for row in splitdata: 
        counter+=1
        total= total+float(row[1])
        if pointer is not 0:
            difference=float(row[1])-pointer
            add+=difference
            if difference>grincrease:
                grincrease=difference
                incmonth=(row[0])
            elif difference<grdecrease:
                grdecrease=difference
                decmonth=(row[0])
                pass
        difference=0
        pointer=float(row[1])
    average=add/(counter)
    print("Financial Analysis")
    print("............................")
    print("Total months: " +str(math.ceil(counter)))
    print("Total: $"+str(math.ceil(total)))
    print("Average change: $"+str(math.ceil(average)))
    print("Greatest increase in profits:"+incmonth+"(" +str(math.ceil(grincrease))+")")
    print("Greatest decrease in profit:"+decmonth+"("+str(math.ceil(grdecrease))+")")