# Inputs
deposit = 300.445
years = 3.25
rate = 0.03

# Calculations
interest = deposit * (1 + rate) ** years
total = deposit + interest

# Round to 2 decimals
years = round(years,2)
rate = round(rate,2)
deposit =round(deposit,2)
interest = round(interest, 2)
total = round(total, 2)

# Create the output
label1 = 'Rate'
label2 = 'Deposit'
label3 = 'Interest'
label4 = 'Total'

title = str(years) + ' YEAR PROJECTION'

line1 = label1.ljust(15, '.') + str(rate) + '%'
line2 = label2.ljust(15, '.') + '$' + str(deposit)
line3 = label3.ljust(15, '.') + '$' + str(interest)
line4 = label4.ljust(15, '.') + '$' + str(total)

print(title)
print()
print(line1)
print()
print(line2)
print(line3)
print(line4)