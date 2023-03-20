# declare meal variable and assign value
meal = 44.50
# calculate percentage by doing 6.75 divide by 100 to get percentage as decimal
tax = float(6.75)/100
# print(tax)
tip = float(15.0)/100
# print(tip)
# re-assing meal value with tax added on
meal += meal * tax
# print(meal)
total = meal + meal * tip
print(total)