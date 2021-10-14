import os
import csv
#filepath = "/Users/gurbindesidhu/Desktop/Pythonhomework/pythonchallenges/Pybank.py/Resources/budget_data.csv"
filepath = "./Resources/budget_data.csv"
profit = []
monthly_changes = []
date = []
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0
average_change_profits = 0
total_loss=0
initial_loss = 0
total_change_losses=0
average_change_losses =0
total_months = 0
total_net = 0
average_change=0


with open(filepath) as csv_file:

    #print (csv_file)

    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    #print(csv_header)
    
    for row in csv_reader:
          print(row)
          total_months = total_months + 1
          total_net = total_net + int(row[1])
          #average_change= total_net/total_months
          count=count+1
          date.append(row[0])
          total_profit = total_profit + int(row[1])
          final_profit=int(row[1])
          monthly_change_profit=final_profit - initial_profit
          monthly_changes.append(monthly_change_profit)
          total_change_profits=total_change_profits + monthly_change_profit
          initial_profit = final_profit
average_change_profits = (total_change_profits/(count))
          
        
          
          #average_change=average_change_profits-average_change_losses
greatest_increase_profits = max(monthly_changes)
greatest_decrease_profits = min(monthly_changes)
        #   increase_date = date[monthly_changes.index(greatest_increase_profits)]
        #   decrease_date = date[monthly_changes.index(greatest_decrease_profits)]


print(monthly_change_profit)
print(f"total months:{total_months}")
print(f"total net:${total_net}")
print(f"average change profits:{average_change_profits}")
#print(f"average change losses:{average_change_losses}")
print(f"greatest increase profits:${greatest_increase_profits}")
print(f"greatest decrease profits:${greatest_decrease_profits}")
# print(f"increase date:{increase_date}")
# print(f"decrease date:{decrease_date}")


    # track total months
    # track net change
    # Greatest increase
    # greatest decrease  
File_to_write = "./analysis/budget_data.txt" 
with open(File_to_write,"w") as f:
        f.write(
f"""
Financial Analysis
-----------------------------
Total months:{total_months}
Total net:${total_net}
Greatest increase profits:${greatest_increase_profits}
Greatest decrease profits:${greatest_decrease_profits}

"""

        )