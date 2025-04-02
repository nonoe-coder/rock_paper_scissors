
import random
choices=['rock','paper','scissors']  

userinput= input(" your choice")
computerchoice= random.choice(choices)


# if userinput==('paper') and  (computerchoice=='scissors'):
#         print (f"computer chose:{computerchoice}")
#         print("you loose")
# elif(userinput=="scissors") and (computerchoice=="rock"):
#         print (f"computer chose:{computerchoice}")
#         print("you loose")
# elif(userinput=="rock")  and (computerchoice=="paper"):
#         print (f"computer chose:{computerchoice}")
        # print("you loose")
while True:
        userinput= input(" your choice")
        if userinput != computerchoice:
             print (f"computer chose:{computerchoice}")
             print("you loose")
        else:
             if userinput==computerchoice:
                print (f"computer chose:{computerchoice}")
                print("you have a tie")




