import random
while True:
    print("\033[1m" + "\n\nYou need to select from these.\n"
                      "1.rock\n"
                      "2.paper\n"
                      "3.scissors\n" + "\033[0m")

    select = (input("Select : "))
    if select == "1":
        print(f"You selected {select}:rock")
    elif select == "2":
        print(f"You selected {select}:paper")
    elif select == "3":
        print(f"You selected {select}: scissors")

    computer_select = random.randint(1, 3)
    if computer_select == 1:
        print(f"Computer selected {computer_select}:rock")
    elif computer_select == 2:
        print(f"Computer selected {computer_select}:paper")
    elif computer_select == 3:
        print(f"Computer selected {computer_select}:scissors")
    else:
        pass

    if select == "1" and computer_select == 1:
        print("\n\tExit")
    elif select == '2' and computer_select == 2:
        print("\n\tExit")
    elif select == '3' and computer_select == 3:
        print("\n\tExit")

    if select == '1' and computer_select == 3:
        print(f"Rock breaks scissors\nYou Win")

    elif select == '3' and computer_select == 1:
        print(f"Rock breaks scissors\nYou Loss")

    elif select == '2' and computer_select == 3:
        print("Scissors cuts paper\nYou Loss")

    elif select == '3' and computer_select == 2:
        print("Scissors cuts paper\nYou Win")

    elif select == '1' and computer_select == 2:
        print("Paper covers rock\nYou Loss")

    elif select == '2' and computer_select == 1:
        print("Paper covers rock\nYou Win")

    print("\033[1m" + "\n\nGame Over\t" + "\033[0m")
