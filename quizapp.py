
while True:
    score = 0

    name =input("Enter your name")
    print("welcome MR . " + name + " to the quiz!")


    print("\n1. How many players are in a cricket team?")
    print("A. 9")
    print("B. 10")
    print("C. 11")
    print("D. 12")

    answer = input("Choose A/B/C/D or E to exit: ").upper()
    if answer == "E":
        exit()
    elif answer == "C":
        print("Correct!")
        score += 1
    else:
        print("Wrong! Answer is C")

    print("\n2. How many balls are in an over?")
    print("A. 4")
    print("B. 6")
    print("C. 8")
    print("D. 10")

    answer = input("Choose A/B/C/D or E to exit: ").upper()
    if answer == "E":
        exit()
    elif answer == "B":
        print("Correct!")
        score += 1
    else:
        print("Wrong! Answer is B")

    print("\n3. Which country won the 2024 T20 World Cup?")
    print("A. Australia")
    print("B. India")
    print("C. England")
    print("D. Pakistan")

    answer = input("Choose A/B/C/D or E to exit: ").upper()
    if answer == "E":
        exit()
    elif answer == "B":
        print("Correct!")
        score += 1
    else:
        print("Wrong! Answer is B")

    print("\nYour final score:", score, "/3")

    if score == 3:
        print("congratulations all three is correct, percentage 100")
    elif score == 2:
        print("65%")
    elif score == 1:
        print("35%")
    else:
        print("better luck next time practice more")

    play_again = input("\nDo you want to play again? (yes/no): ")

    if play_again != "yes":
        print("thanks for playing")
        break
