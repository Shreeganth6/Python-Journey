import random
import time

start_time = time.time()
end_time = start_time + 180

system_point = 0
player_point = 0

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
loop_condition = True

while loop_condition:

    current_time = time.time()

    if current_time >= end_time:
        if system_point > player_point:
            print("time is over \n You have Lost")
            break
        if system_point < player_point:
            print("Time is over \n You have Won")
            break

    choice = input("\nRock , Paper or Scissor? \n ")
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

    #points --

    if (choice == "rock" and system_choice == paper):
        print("You have lost")
        player_point = player_point - 1
        system_point = system_point + 1
        print(f"you are having {player_point} points")

    elif (choice == "paper" and system_choice == scissor):
        print("You have lost")
        player_point = player_point - 1
        system_point = system_point + 1
        print(f"you are having {player_point} points")

    elif (choice == "scissor" and system_choice == rock):
        print("You have lost")
        player_point = player_point - 1
        system_point = system_point + 1
        print(f"you are having {player_point} points")

    # points ++

    if (choice == "rock" and system_choice == scissor):
        print("You have won this round")
        player_point = player_point + 1
        system_point = system_point - 1
        print(f"you are having {player_point} points")

    elif (choice == "paper" and system_choice == rock):
        print("You have won this round")
        player_point = player_point + 1
        system_point = system_point - 1
        print(f"you are having {player_point} points")

    elif (choice == "scissor" and system_choice == paper):
        print("You have won this round")
        player_point = player_point + 1
        system_point = system_point - 1
        print(f"you are having {player_point} points")

    # points draw

    if (choice == "rock" and system_choice == rock):
        print("Ended up in draw for this round")
        print(f" {player_point} points")

    elif (choice == "paper" and system_choice == paper):
        print("Ended up in draw for this round")
        print(f" {player_point} points")

    elif (choice == "scissor" and system_choice == scissor):
        print("Ended up in draw for this round")
        print(f" {player_point} points")

    # game results

    if player_point == 5:
        print("the player has won the match ")
        break

    if player_point == -5:
        print("The computer has won the match")
        break