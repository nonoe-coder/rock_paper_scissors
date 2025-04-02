import random 
choices=["rock","paper","scissors"]
user_choice =input ("whats your choice")
computer_choices = random.choice (choices)

print (f"computer chose:{computer_choices}")
if choice==computer_choices:
      print("tie")
                    
else: 
      print ("lose")