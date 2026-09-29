import random

while True:
    while True:
        try:
            number = int(input("How many rolls do you want to make? "))
            n = number
            break
        except ValueError:
            print("Enter a valid number")

    while n != 0:
        if n == 1:
            print(f"you have {n} dice left")
        else:
            print(f"you have {n} dices left")

        choice = input("Roll the dice? (y/n): ").lower()
        if choice == "y":
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            print(f"({die1}, {die2})")
            n = n - 1

        elif choice == "n":
            break

        else:
            print("plaese enter y or n, y: yes and n: no")

    print("you have finished your game")

    again = input("Do you want to play again? if yes write (y): ").lower()
    if again != "y":
        print("Thank you for playing")
        break


#just a note i created this code with the help of this video:
#https://www.youtube.com/watch?v=yVl_G-F7m8c&t=1098s