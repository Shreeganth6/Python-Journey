import random

points = 0
print("Welcome to Rock Paper Scissor game ")
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
while (points > -3 and points < 3):
    choice = input("\nRock , Paper or Scissor? ")
    choice = choice.lower()
    if choice == "rock":
        print("\n" + rock)

    elif choice == "paper":
        print("\n" + paper)

    elif choice == "scissor":
        print("\n" + scissor)

    else:
        print("Enter a valid option!")
        continue

    print("The computer choice is : ")
    game = [rock, paper, scissor]
    random_num = random.randint(0, 2)
    system_choice = game[random_num]
    print(system_choice)

    if (choice == "rock" and system_choice == paper):
        print("You have lost")
        points = points - 1
        print(f"you are having {points} points")

    elif (choice == "paper" and system_choice == scissor):
        print("You have lost")
        points = points - 1
        print(f"you are having {points} points")

    elif (choice == "scissor" and system_choice == rock):
        print("You have lost")
        points = points - 1
        print(f"you are having {points} points")

    # points ++

    if (choice == "rock" and system_choice == scissor):
        print("You have won this round")
        points = points + 1
        print(f"you are having {points} points")

    elif (choice == "paper" and system_choice == rock):
        print("You have won this round")
        points = points + 1
        print(f"you are having {points} points")

    elif (choice == "scissor" and system_choice == paper):
        print("You have won this round")
        points = points + 1
        print(f"you are having {points} points")

    # points draw

    if (choice == "rock" and system_choice == rock):
        print("Ended up in draw for this round")
        print(f"+ {points} points")

    elif (choice == "paper" and system_choice == paper):
        print("Ended up in draw for this round")
        print(f"+ {points} points")

    elif (choice == "scissor" and system_choice == scissor):
        print("Ended up in draw for this round")
        print(f"+ {points} points")

    # game results

    if points == 3:
        print("the player has won the match ")
        break

    if points == -3:
        print("The computer has won the match")
        break