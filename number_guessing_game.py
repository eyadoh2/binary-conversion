import random

print("from what number to what number do you want the guessing game to be? ")

while True:
    try:
        min = int(input("first number: "))
        break
    except ValueError:
            print("Enter a number only")  

while True:
    try:
        max = int(input("last number: "))
        if max < min or max == min:
             print("the last number must be greater than the first number")
        else:
             break
    except ValueError:
            print("Enter a number only")

n = random.randint(min, max)
track = 0
while True:
    try:
        number = int(input(f"Guess the number between {min} and {max}: "))
        track = track + 1

        if number > max or number < min:
            print(f"Enter a number between {min} and {max} only")

        elif number > n:
            print("your number is bigger")

        elif number < n:
            print("your number is smaller")

        elif number == n:
            print(f"the number is {n} you gussed it correctly after {track} times")
            again = input("do you want to play again? if yes write y: ").lower()
            if again != "y":
                print("thank you")
                break

    except ValueError:
        print("Enter a number only")


#just a note i created this code with the help of this video:
#https://www.youtube.com/watch?v=yVl_G-F7m8c&t=1098s