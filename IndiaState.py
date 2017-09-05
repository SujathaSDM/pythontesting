capital_dict = {'Andrapradesh' : 'Amaravati','Telengana' : 'Hyderbad', 'Karnataka' : 'Bangalore', 'TamilNadu' : 'Chenni', 'Kerala' : 'Thiruvananthapuram', 'Orissa' : 'Bhubaneshwar','West Bengal' : 'Culcutta', 'Uttar Pradesk' : 'Laknow','Maharastra' : 'Mumbai', 'Gujarat' : 'Gandhinagar'}

import random

states = list(capital_dict.keys())

for i in [1,2,3,4,5,6,7,8,9,10]:
    state = random.choice(states)
    capital = capital_dict[state]
    capital_guess = input("What is the capital of " + state +" ?")

    if capital_guess == capital:
       print("Correct! Nice job.")
    else:
       print("Incorrect. The Capital of "+state+" is " + capital + " . ")

print("All done")

