# Importing Modules
import os
import csv

# Setting path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Create empty lists to store data
date = []
profit_losses = []
current_month = []
last_month = []
average_change = []

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header
    header = next(csvreader)
   
     # Loop through looking for the video
    for row in csvreader:

        # Add months from first row to date, and profit_losses from second row to profit_losses
        date.append(row[0])
        profit_losses.append(int(row[1])) 
        
    # Total number of months
    total_months = len(date)
        
    # Net total of profit and losses
    total_profit_losses = sum(profit_losses)


# Create list for current month revenue, skip first value
current_month = profit_losses[1:]
# Create list for last month revenue including all, but the last value
last_month = profit_losses[:-1]

# Combine current and last month by creating list that zips both lists
List_average_change = [current - last    for (current, last) in zip(current_month, last_month)]

# Calculate the amount change between each month by
average_change = round(sum(List_average_change)/len(List_average_change), 2)

# Calculate the greatest increase value and month
greatest_increase_value = max(List_average_change)
greatest_increase_month = date[List_average_change.index(greatest_increase_value)]

# Calculate the greatest decrease value and month
greatest_decrease_value = min(List_average_change)
greatest_decrease_month = date[List_average_change.index(greatest_decrease_value)]

# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {str(total_months)}\n"
    f"Total: ${total_profit_losses:,}\n"
    f"Average Change: ${average_change:,.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_value:,.2f})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_value:,.2f})\n")
        
# Print the output to terminal
print(output)

# Export the results to text file
file = "PyBank_Report.txt"
with open(file, "w") as f:
    f.write(output)









   

     
        
     


    