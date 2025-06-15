import random

def spin_the_wheel():
    print("🎡 Welcome to Spin the Wheel - Guess the Number!")
    min_number = 1
    max_number = 10
    secret_number = random.randint(min_number, max_number)
    
    try:
        guess = int(input(f"Guess the number between {min_number} and {max_number}: "))
    except ValueError:
        print("⚠️ Invalid input! Please enter a number.")
        return
    
    print(f"The wheel spun... and landed on {secret_number}!")

    if guess == secret_number:
        print("🎉 Congratulations! You guessed it right!")
    else:
        print("❌ Sorry, better luck next time!")

if __name__ == "__main__":
    spin_the_wheel()