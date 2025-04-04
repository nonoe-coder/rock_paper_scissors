import random

def get_random_doors():
    """Randomly assign doors to the lion, river, and treasure."""
    doors = ["lion", "river", "treasure"]
    random.shuffle(doors)
    return { "red": doors[0], "blue": doors[1], "green": doors[2] }

def get_clue(door_mapping):
    """Provide a clue that hints at what is behind the doors."""
    danger_doors = [door for door, content in door_mapping.items() if content in ["lion", "river"]]
    safe_door = [door for door, content in door_mapping.items() if content == "treasure"][0]

    # Randomly select a dangerous door to hint about
    hint_door = random.choice(danger_doors)
    hint = f"Avoid the {hint_door} door! Something dangerous might be there."
    
    return hint, safe_door

def play_game():
    score = 3  # Player starts with 3 points
    lives = 3  # Player starts with 3 lives

    print("🎉 Welcome to the Treasure Hunt! 🏆")
    print("Behind one of these doors is a hidden treasure!")
    print("Choose wisely: Red, Blue, or Green.")
    print(f"\n💰 You start with {score} points and ❤️ {lives} lives.")

    while lives > 0:
        door_mapping = get_random_doors()
        clue, treasure_door = get_clue(door_mapping)

        print("\n🔍 Here's a clue to help you: ")
        print(clue)

        player_choice = input("\nEnter your choice (Red/Blue/Green): ").strip().lower()

        if player_choice in door_mapping:
            result = door_mapping[player_choice]
            if result == "treasure":
                score += 2  # Gain points for finding the treasure
                print("\n🎉 Congratulations! You found the treasure! 🏆")
            elif result == "lion":
                score -= 2  # Lose points for encountering a lion
                lives -= 1  # Lose a life
                print("\n🦁 Oh no! A lion jumps out! You lose a life!")
            else:
                score -= 1  # Lose fewer points for falling into the river
                lives -= 1  # Lose a life
                print("\n🌊 You fell into a river! You lose a life!")

            print(f"💰 Score: {score} | ❤️ Lives remaining: {lives}")

            if lives == 0:
                print("\n💀 Game Over! You ran out of lives.")
                break  # End the game if lives reach 0

            print("\n🔁 Do you want to play again?")
            replay = input("Type 'yes' to continue or anything else to quit: ").strip().lower()
            if replay != "yes":
                print("\n👋 Thanks for playing! See you next time!")
                break

        else:
            print("\n🚪 Invalid choice! Please choose Red, Blue, or Green.")

if __name__ == "__main__":
    play_game()
