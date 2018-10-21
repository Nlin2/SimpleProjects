# Calculates tax on bill
meal = float(input('Price of meal: '))
tax =  float(input('Tax Percent at your location: ')) / 100
tip = float(input('Tip Percentage: ')) / 100
meal = meal + meal * tax
total = meal + meal * tip
print('Your total amount is: ' + str(total))
