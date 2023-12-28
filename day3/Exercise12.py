print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name1 = name1.lower()
name2=name2.lower()
occursT1 = name1.count("t",0)
occursT2 = name2.count("t",0)
occursR1 = name1.count("r",0)
occursR2 = name2.count("r",0)
occursU1 = name1.count("u",0)
occursU2 = name2.count("u",0)
occursE1 = name1.count("e",0)
occursE2 = name2.count("e",0)

occursL1 = name1.count("l",0)
occursL2 = name2.count("l",0)
occursO1 = name1.count("o",0)
occursO2 = name2.count("o",0)
occursV1 = name1.count("v",0)
occursV2 = name2.count("v",0)
true = str(occursT1 + occursT2 + occursR1 + occursR2 + occursU1 + occursU2 + occursE1 + occursE2)
Love = str(occursL1 + occursL2 + occursO1 + occursO2 + occursV1 + occursV2+ occursE1 + occursE2)
total = int(true+Love)
if total < 10 or total >90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >=40 and total <=50:
    print(f"Your score is {total}, you are alright together.")
else: 
    print(f"Your score is {total}.")