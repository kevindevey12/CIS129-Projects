# Author: Kevin Devey
# Module 3 Lab
# Coffee Shop Simulator
# Updated to include more menu items

#Print and ask for inputs
print('***********************************')
print('My Coffee and Muffin Shop')
Coffee = int(input("Number of coffees bought?\n"))
Muffins = int(input("Number of muffins bought?\n"))
Cookies = int(input("Number of cookies bought?\n"))
Juice = int(input("Number of juices bought?\n"))
print('***********************************')
print('\n')
print('***********************************')
#Print and generate receipt
print('My Coffee and Muffin Shop Receipt')
print(Coffee,"Coffee(s) at $5 each: $",Coffee*5)
print(Muffins,"Muffin(s) at $4 each: $",Muffins*4)
print(Cookies,"Cookie(s) at $2 each: $",Cookies*2)
print(Juice,"Juice(s) at $3 each: $",Juice*3)
Tax = round(float(.06*((Coffee*5)+(Muffins*4)+(Cookies*2)+(Juice*3))),2)
Total = round((Coffee*5)+(Muffins*4)+(Cookies*2)+(Juice*3)+Tax,2)
print('6% tax: $', round(Tax,2))
print('---------')
print('Total: $',round(Total,2))
print('***********************************')
print('Thank you for your order!')
print('Come again')
