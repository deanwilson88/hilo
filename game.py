from random import randint


def main():
    print("Welcome to the HI - LO game")
    print("Guess a number between 1 & 100: ", end="")

    answer = randint(1, 101)
    guess = 0

    while not guess == answer:
        guess = int(input())
        if guess == answer:
            print("Got it, the number is {}".format(answer))
            break
        elif guess < answer:
            print("Too low!")
        else:
            print("Too high!")


if __name__ == "__main__":
    main()
