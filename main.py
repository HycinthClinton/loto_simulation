numbers = [7, 100, 50, 14]


def loto_simulation():
    try:
        print("Welcome to the Loto Simulation!")
        for attempt in range(3):
            try:
                guess = int(input("Guess a number: "))

                if guess in numbers:
                    print("correct!")
                    print("well done.")
                    break

                elif guess not in numbers:
                    print("Incorrect, try again!\n")
            except ValueError:
                print("Please enter a valid number!\n")

        else:
            print("Game over, attempt exhausted!")

    except Exception as e:
        print(e)


loto_simulation()
