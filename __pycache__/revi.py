def adventure_game():
    print("Welcome to the Adventure Game!")
    name = input("What's your name, adventurer? ")
    print(f"Hello {name}, your journey begins now!\n")
    
    # First decision: left or right?
    choice = input("You come to a fork in the road. Do you go left or right? ").lower().strip()
    if choice == "left":
        print("\nYou walk along the left path and find a peaceful village.")
        second_choice = input("The villagers offer you food and shelter. Do you stay or continue your journey? (stay/continue) ").lower().strip()
        if second_choice == "stay":
            print("\nYou decide to rest in the village and recover your strength. A wise elder shares tales of hidden treasures.")
        elif second_choice == "continue":
            print("\nYou bid farewell to the villagers and continue your journey with newfound hope!")
        else:
            print("\nUnable to decide, you wander around the village until you eventually move on, a little lost.")
    elif choice == "right":
        print("\nYou take the right path and encounter a mysterious traveler.")
        second_choice = input("The traveler offers you a map to hidden treasure. Do you accept the map or decline? (accept/decline) ").lower().strip()
        if second_choice == "accept":
            print("\nWith the map in hand, you feel your chances of finding treasure increase dramatically!")
        elif second_choice == "decline":
            print("\nYou decline the map, choosing to rely on your instincts, though you wonder if you missed an opportunity.")
        else:
            print("\nYour hesitation confuses the traveler, and he vanishes into the mist, leaving you pondering your next move.")
    else:
        print("\nUnable to decide, you wander aimlessly until night falls and you find shelter by chance.")

