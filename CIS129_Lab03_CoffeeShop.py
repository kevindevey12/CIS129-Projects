# Author: Kevin Devey
# Module 3 Lab
# Coffee Shop Simulator

#Print and ask for inputs
print('***********************************')
print('My Coffee and Muffin Shop')
Coffee = input("Number of coffees bought?\n")
Coffee = int(Coffee)
Muffins = input("Number of muffins bought?\n")
Muffins = int(Muffins)
print('***********************************')
print('\n')
print('\n')
print('***********************************')
#Print and generate receipt
print('My Coffee and Muffin Shop Receipt')
print(Coffee,"Coffee(s) at $5 each: $",Coffee*5)
print(Muffins, "Muffin(s) at $4 each: $",Muffins*4)
Tax = float(.06*((Coffee*5)+(Muffins*4)))
Total = (Coffee*5)+(Muffins*4)+Tax
print('6% tax: $', round(Tax,2))
print('---------')
print('Total: $',round(Total,2))
print('***********************************')
