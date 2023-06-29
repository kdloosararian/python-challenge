
import os
import csv

# input path to the CSV file 
csv_path= '/Users/katieloosararian/Class_Requirements/Module 3/Starter_Code/PyBank/Resources/budget_data.csv'

#initializing the variables 
total_months = 0 
net_profit_losses = 0
changes = []
greatest_increase = ['', 0]
greatest_decrease = ['',0] 

#Read on csv file
with open(csv_path, 'r') as file:
    csv_reader = csv.reader(file,delimiter= ',')
    header = next(csv_reader)

    #iterate the rows over
    for row in csv_reader:
        #counting the # of months
        total_months +=1

        #calculate the net total of profit/losses
        net_profit_losses += int(row[1])

        #calculate the changes in profit/ losses over the entire time period
        previous_profit = int(row[1])

        if total_months > 1:
            current_change = int(row[1]) - previous_profit
            changes.append(current_change)


            #find greatest invcrease in profits
            if current_change > greatest_increase[1]:
                greatest_increase = [row[0], current_change]

          
#calculate the average change, set variable
average_change =  sum(changes) / len(changes)

# print out the results 
print(f"Total number of months: {total_months}")
print(f"Net total amount of Profit/Losses: ${net_profit_losses}")
print(f"Average change in Profit/Losses: ${average_change:.2f}")
print(f"Greatest increase in profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest decrease in profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

