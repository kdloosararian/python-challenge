import os
import csv

# Path to the CSV file
csv_path = '/Users/katieloosararian/Class_Requirements/Module 3/Starter_Code/PyBank/Resources/budget_data.csv'

# Initialize variables
total_months = 0
net_profit_losses = 0
changes = []
greatest_increase = ['', 0]
greatest_decrease = ['', 0]

# Read the CSV file
with open(csv_path, 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    header = next(csv_reader)

    # Iterate over the rows
    for row in csv_reader:
        # Count the number of months
        total_months += 1

        # Calculate the net total amount of "Profit/Losses"
        net_profit_losses += int(row[1])

        # Calculate the changes in "Profit/Losses" over the entire period
        if total_months > 1:
            current_change = int(row[1]) - previous_profit
            changes.append(current_change)

            # Find the greatest increase in profits
            if current_change > greatest_increase[1]:
                greatest_increase = [row[0], current_change]

            # Find the greatest decrease in profits
            if current_change < greatest_decrease[1]:
                greatest_decrease = [row[0], current_change]

        previous_profit = int(row[1])

# Calculate the average change
average_change = sum(changes) / len(changes)

# Print the results
print(f"Total number of months: {total_months}")
print(f"Net total amount of Profit/Losses: ${net_profit_losses}")
print(f"Average change in Profit/Losses: ${average_change:.2f}")
print(f"Greatest increase in profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest decrease in profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
