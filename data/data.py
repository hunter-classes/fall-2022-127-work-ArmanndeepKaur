import csv

with open('avocado.csv', 'r') as csv_file:
  csv_reader = csv.reader(csv_file)
  for line in csv_reader:
    print(line)
    
print()

import pandas as pd
df = pd.read_csv("avocado.csv")

#Finding the Range of different things in the datatset
print("The range of average avacado price is:", df.AveragePrice.max()-df.AveragePrice.min())
print("The range of total bags:", df.TotalBags.max()-df.TotalBags.min())
print("The range of small bags:", df.SmallBags.max()-df.SmallBags.min())
print("The range of large bags:", df.LargeBags.max()-df.LargeBags.min())
print("The range of XLarge bags:", df.XLargeBags.max()-df.XLargeBags.min())

print()

#Finding the Frequency of different things in the dataset
print("The frequency of avocado types:")
print(df['type'].value_counts())
print()
print("The frequency of regions:")
print(df['region'].value_counts())

#Extra
#KaiMinY helped me with the plotting 

import matplotlib.pyplot as plt 

x = []
y = []

with open('avocado.csv', 'r') as csvfile:
  plots = csv.reader(csvfile, delimiter = ",")
  
  for row in plots:
    x.append(row[12])
    y.append(row[2])

plt.bar(x,y, color = 'g', width = 0.72, label = "Year")
plt.xlabel('Year')
plt.ylabel('AveragePrice')
plt.title('Avocado prices in different years')
plt.legend()
plt.show()