#make a tip calculator- we will need a place to store our input
print('Welcom to the tip calculator.')

total_bill = float(input('What was the total bill?'))

# percentage of a tip being given a multitude of choices like 15% or 20%

tip = float(input('What is the percentage you want to tip?'))

people_split = int(input('How many people will be splitting the bill?'))

final_tip = (tip/100) + 1

bill_split = (total_bill / people_split) * final_tip

tip_per_person = (total_bill * (tip/100) / people_split)

round_tip_per_person = round(tip_per_person, 2)

total_bill_with_tip = round(bill_split, 2)

total_bill_agg = total_bill * final_tip

print('Total tip per person is ' + str(round_tip_per_person))
print('Total bill per person is ' + str(total_bill_with_tip))
print('Total bill is ' + str(total_bill_agg))
