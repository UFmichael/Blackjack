#a game of blackjack
#assumption 1: you are pulling from an infinite deck of cards
#assumption 2: aces only hold the value "1"
#Last Modified: 7/19/2022

import random

more_play = True

game_number = 0

wins = 0

losses = 0

ties = 0

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list2 = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

#pick a random number from list 1 which corresponds to a card
def random_card():
  return random.choice(list1)

#identify the type of card
def card_type(x):
  if x == 1:
    type = "ACE"
  elif x == 11:
    type = "JACK"
  elif x == 12:
    type = "QUEEN"
  elif x == 13:
    type = "KING"
  else:
    type = x
  
  return type

#return the blackjack value of a card
def card_value(x):
  if x == 1:
    type = 1
  elif x == 11:
    type = 10
  elif x == 12:
    type = 10
  elif x == 13:
    type = 10
  else:
    type = x
  return type

#generate the value of the dealer's hand
def dealer_hand():
  return random.choice(list2)

#main part for continuing the loop
while more_play:
  game_number += 1
  print("\n\nStart Game #"+str(game_number))
  b = 3 #random_card()
  value = int(card_value(b))
  card1 = card_type(b)
  print("Your card is a " + str(card1) + "!")

  round = True

  #Keeps the round going when it has not ended
  while round:
    
    print("Your current hand has a value of "+ str(value) +".")
    print("1. Get another card \n2. Hold hand \n3. Print statistics \n4. Exit")
    
    #checks if the player's hand is over 21
    if value > 21:
      print("You exceeded 21! You lose.")
      round = False
      losses += 1
    #checks if the player has a blackjack
    elif value == 21:
      print("BLACKJACK! You win!")
      round = False
      wins += 1
    else:

      valid = True
      
      while valid:
        
        choice = int(input())

        if choice == 1:
          valid = False
        elif choice == 2:
          valid = False
        elif choice == 3:
          valid = False
        elif choice == 4:
          valid = False
        else:
          print("Invalid input! \nPlease enter an integer value between 1 and 4.")

      #gives player another card
      if choice == 1:
        b = random_card()
        card_add = card_type(b)
        print("\nYour card is a " + str(card_add) + "!")
        value += int(card_value(b))

      #sees who wins the round
      if choice == 2:
        round = False
        dealer = dealer_hand()
        if int(dealer) > 21:
          print("You win!")
          wins += 1
        elif int(dealer) == value:
          print("It's a tie! No one wins!")
          ties += 1
        elif int(dealer) < value:
          print("You win!")
          wins += 1
        else:
          print("Dealer wins!")
          losses += 1
      
      if choice == 3:
        games_played = game_number - 1
        print("\nYou have played " + str(games_played) + " games.")
        print("You have won "+ str(wins) + " games.")
        print("You have lost "+ str(losses) + " games.")
        print("You have tied " + str(ties) + " games.")

      if choice == 4:
        print("\n\nThank you for playing! Have a wonderful day!")
        round = False
        more_play = False
        
