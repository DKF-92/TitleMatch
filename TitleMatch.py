#For this program we want to loop through a csv file searching for a keyword, 
#if this keyword is found a new list will be made with a string that contains the keyword

# Imports libraries and dependencies
import csv
import string
import pandas as pd

#Sets the keyword to be found
keyword = ('letham')

#Imports data
summary_file = 'TitleMatch\SummaryTitles.csv'
outputFile = []

#Opens csv file
with open(summary_file, 'r') as csvfile:
    dataReader = [line.lower() for line in csvfile]
    
    #loops through csv file
    for row in dataReader:
        if 'letham' in row:
            outputFile.append(str(row).replace("\n",""))

df = pd.DataFrame([[outputFile]])
df.columns = ['Site Name']
df.to_csv("TitleMatch\Test123.csv", sep='\t', index=False)

print(outputFile)