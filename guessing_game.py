import random
import time

def start_game():
    print("\n" + "="*35)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("="*35)

    # 1. Difficulty Selection
    print("\nPlease select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    
    choice = input("Enter your choice (1/2/3): ")
    
    chances = 10 if choice == '1' else 5 if choice == '2' else 3
    level = "Easy" if choice == '1' else "Medium" if choice == '2' else "Hard"
    
    print(f"\nGreat! You selected {level} difficulty. You have {chances} chances.")
    print("Let's start the game!")

    # 2. Game Setup
    secret_number = random.randint(1, 100)
    attempts = 0
    start_time = time.time()

    # 3. Game Loop
    while attempts < chances:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1
            
            if guess == secret_number:
                end_time = time.time()
                total_time = round(end_time - start_time, 2)
                print(f"🎉 Congratulations! You guessed the correct number in {attempts} attempts.")
                print(f"⏱️ Time taken: {total_time} seconds.")
                return
            elif guess < secret_number:
                print(f"❌ Incorrect! The number is greater than {guess}.")
            else:
                print(f"❌ Incorrect! The number is less than {guess}.")
            
            print(f"Remaining chances: {chances - attempts}")
            
        except ValueError:
            print("⚠️ Invalid input! Please enter a number.")

    print(f"\n💀 Game Over! You ran out of chances. The number was {secret_number}.")

# Main Logic to allow Replay
if __name__ == "__main__":
    while True:
        start_game()
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye.")
            break
