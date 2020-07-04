#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
import csv

total_months = 0
total_pl = 0
date = []
plnumbers = []
revenue = []
max_val = []
min_val = []
value = 0
profit = []
total_change = 0
date_decrease=[]
date_increase=[]
avsum=[]
avchange=[]

csvpath_file= os.path.join("budget_data.csv") 
with open(csvpath_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header=next(csvfile)
    
    for row in csvreader:
    #Total months
        total_months += 1
    #Total Profit/Losses
        total_pl += int(row[1])
        change = int(row[1]) - value
        value = int(row[1])
        profit.append (change)
        date.append(row[0])
        greatest_increase_profit = max(profit)
        greatest_increase_profit_index = profit.index(greatest_increase_profit)
        greatest_decrease_profit = min(profit)
        greatest_decrease_profit_index = profit.index(greatest_decrease_profit)
        date_decrease=date[greatest_decrease_profit_index]
        date_increase=date[greatest_increase_profit_index] 
    
    profit.pop(0)
    avchange = sum(profit) / len(profit) 
    
    print ("financial analysis")
    print ("total number of months:" + str(total_months) + "months")
    print(f"Total Profit/loss: ${str(total_pl)}")
    print(f"Average Change: ${str(avchange)}")
    print(f"Greatest Increase in Profits: {str(date_increase)} ${str(greatest_increase_profit)}")
    print(f"Greatest Decrease in Profits: {str(date_decrease)} ${str(greatest_decrease_profit)}")

    output=open("results.text", "w")
    line1 = str("financial analysis")
    line2 = str("total number of months:" + str(total_months) + "months")
    line3 =str(f"Total Profit/loss: ${str(total_pl)}")
    line4 = str(f"Average Change: ${str(avchange)}")
    line5 =str(f"Greatest Increase in Profits: {str(date_increase)} ${str(greatest_increase_profit)}")
    line6 =str(f"Greatest Decrease in Profits: {str(date_decrease)} ${str(greatest_decrease_profit)}")
    
    output.write('{}\n {}\n {}\n {}\n {}\n {}\n'.format(line1, line2, line3, line4, line5, line6))


# In[ ]:





# In[ ]:




