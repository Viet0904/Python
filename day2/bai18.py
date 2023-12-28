print("Wellcome to the tip calculator.")
total = float(input("What was the total bill? "))
people = int(input("How many people split the bill? "))
percent = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
moneyperson = total/people
eachperson =  round(moneyperson + moneyperson*(percent/100),2)
print("Each person should pay: " + "$" +str(eachperson) )
