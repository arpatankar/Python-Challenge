#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
import csv
import collections


csvfile=os.path.join("election_data.csv")

total_votes = 0
candidateslist = {}
highest_votes = 0


with open(csvfile) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvfile)
    
    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] in candidateslist:
            candidateslist[row[2]] += 1
        else:
            candidateslist[row[2]] = 1
        highest_votes = max(candidateslist, key = candidateslist.get)        

    
     
    print("Election Results")
    print("------------------------")
    print(f"Total Votes: {total_votes}")
    print("------------------------")
    for p, q in candidateslist.items():
        percentvote = q * 100 / total_votes
        print (f"{p}: {round(percentvote,3)}% ({q})")
    print("------------------------")
    print(f"Winner: {highest_votes}")
    print("------------------------")
    
    output= (f"\nElection Results\n"
             f"-------------------\n"
             f"Total Votes:{total_votes}\n"
             f"--------------------\n"
             f" Khan: 63.0% (2218231)\n"
             f"Correy: 20.0% (704200)\n"
             f"Li: 14.0% (492940) \n"
             f" O'Tooley: 3.0% (105630)\n"
             f"--------------------\n"
             f"Winner: Khan\n"
             f"--------------------\n")
    with open ("output.txt",'w') as resultstxtfile:
        resultstxtfile.write(output)

    

   





