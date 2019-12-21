# Introduction
print("Bored of the game 'Rock, Paper, Scissors'? ")
print("Then try out this new, unusual game of 'Rock, Paper, Scissors, Lizard, Spock!")
print("""
      It's very simple,
      Scissors cuts paper.
      Paper covers rock.
      Rock crushes lizard.
      Lizard poisons Spock.
      Spock smashes scissors.
      Scissors decapitates lizard.
      Lizard eats paper.
      Paper disproves Spock.
      Spock vaporizes rock.
      And as it always has,
      Rock crushes scissors.
       """)

import random
game=['rock','paper','scissors','lizard','spock']


C_score = 0
P_score = 0

for x in range (10):
   round = print(f'Round {x+1}')
   player = input("What is your choice - Rock, Paper, Scissors, Lizard, or Spock? \n").lower()
   computer = random.choice(game)

   if computer == 'rock':

       if player == computer:
         print("It's a Draw")
       elif player == 'paper':
         print(f"""Bazinga, You Won!
                   The Computer chose {computer}.""")
         P_score += 1
       elif player == 'spock':
         print(f"""Bazinga, You Won!
                   The Computer chose {computer}.""")
         P_score += 1
       elif player == 'scissors':
         print(f"You Lost. The Computer chose {computer}")
         C_score += 1
       elif player == 'lizard':
         print(f"You Lost. The Computer chose {computer}")
         C_score += 1
       else:
         print("Sorry!! You have entered a wrong choice. Restart the Game")

   elif computer == 'paper':

        if player == computer:
          print("It's a Draw")
        elif player == 'scissors':
          print(f"""Bazinga, You Won!
                    The Computer chose {computer}.""")
          P_score += 1
        elif player == 'lizard':
          print(f"""Bazinga, You Won!
                    The Computer chose {computer}.""")
          P_score += 1
        elif player == "spock":
          print(f"You Lost. The Computer chose {computer}")
          C_score += 1
        elif player == "rock":
          print(f"You Lost. The Computer chose {computer}")
          C_score += 1
        else:
          print("Sorry!! You have entered a wrong choice. Restart the Game")

   elif computer == 'scissors':

        if player == computer:
          print("It's a Draw")
        elif player == 'spock':
          print(f"""Bazinga, You Won!
                    The Computer chose {computer}.""")
          P_score += 1
        elif player == 'rock':
          print(f"""Bazinga, You Won!
                    The Computer chose {computer}.""")
          P_score += 1
        elif player == "lizard":
          print(f"You Lost. The Computer chose {computer}")
          C_score += 1
        elif player == "paper":
          print(f"You Lost. The Computer chose {computer}")
          C_score += 1
        else:
          print("Sorry!! You have entered a wrong choice. Restart the Game")

   elif computer == 'lizard':

        if player == computer:
          print("It's a Draw")
        elif player == 'scissors':
          print(f"""Bazinga, You Won!
                    The Computer chose {computer}.""")
          P_score += 1
        elif player == 'rock':
          print(f"""Bazinga, You Won!
                    The Computer chose {computer}.""")
          P_score += 1
        elif player == "spock":
          print(f"You Lost. The Computer chose {computer}")
          C_score += 1
        elif player == "paper":
          print(f"You Lost. The Computer chose {computer}")
          C_score += 1
        else:
          print("Sorry!! You have entered a wrong choice. Restart the Game")

   elif computer == 'spock':

        if player == computer:
          print("It's a Draw")
        elif player == 'paper':
          print(f"""Bazinga, You Won!
                    The Computer chose {computer}.""")
          P_score += 1
        elif player == 'lizard':
          print(f"""Bazinga, You Won!
                    The Computer chose {computer}.""")
          P_score += 1
        elif player == "scissors":
          print(f"You Lost. The Computer chose {computer}")
          C_score += 1
        elif player == "rock":
          print(f"You Lost. The Computer chose {computer}")
          C_score += 1
        else:
          print("Sorry!! You have entered a wrong choice. Restart the Game")


print(f'''
Computer = {C_score}
Player   = {P_score}''')

if P_score == C_score:
    print ("It's a Draw!")
elif P_score > C_score:
    print ("Congrats! You Won!!!")
elif P_score < C_score:
    print ("You Lost!")

import csv
import os.path

print('Leaderboard -- Rock, Paper, Scissors, Lizard, Spock')
print("-" * 30)

fieldnames = ['Name', 'Computer_Score', 'High_Score']

with open("leaderboard.csv", 'r') as csvfile:
    csvReader = csv.DictReader(csvfile, delimiter=',', fieldnames=fieldnames)

    leaderboard = list(csvReader)

    for info in leaderboard:
        print(f'''{info["Name"]:15}
        {info["Computer_Score"]:25} {info["High_Score"]}''')

selection = int(input('''
  Enter Option Number
  --------------------
  1. Add Player to Leaderboard
  2. View Leaderboard
  3. Search for Player
  4. Exit Program
  '''))

if selection == 1:
    name = input('Name of Player:')
    computer = int(input('Computer Score:'))
    player = int(input('Player Score:'))
    save_file(fieldnames, filename)
    view_file(fieldnames, filename)

elif selection == 2:
    view_file(fieldnames, filename)
elif selection == 3:
    search_info = input("Search Leaderboard for: ").title()

    if search_info in open('leaderboard.csv').read():
        print(f"Yes, {search_info} is in the list")
    else:
        print(f"No, {search_info} is not in the list")
    save_file(fieldnames, filename)
    view_file(fieldnames, filename)
elif selection == 4:
    exit()
