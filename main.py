import random as r
attempts = []
even_attempts = []
odd_attempts = []
while True:
    random_num = r.randint(1, 100)
    #print(random_num)
    for i in range(10):
        guess = int(input(f"Attempt {i + 1}: I'm thinking of a number between 1 and 100. You have {10 - i} attempts left: "))
        attempts.append(guess)

        if guess % 2 == 0:
            even_attempts.append(guess)
        else:
            odd_attempts.append(guess)

        if guess == random_num:
            print("\nYou win!")
            print("Game Summary:")
            print(f"You guessed correctly in {len(attempts)} attempts!")
            print(f"Your guesses: {attempts}")
            print(f"Even guesses: {even_attempts}")
            print(f"Odd guesses: {odd_attempts}")
            break

        if guess > random_num:
            print("Too high!")
        elif guess < random_num:
            print("Too low!")

        if i == 9:
            print("\nToo many guesses, you lose.")
            print("Game Summary:")
            print(f"Your guesses: {attempts}")
            print(f"Even guesses: {even_attempts}")
            print(f"Odd guesses: {odd_attempts}")

    again = input("Do you want to play again? (yes/no): ")
    if again == "no":
        break
    attempts = []
    even_attempts = []
    odd_attempts = []