# -*- coding: utf-8 -*-
"""Blackjack Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14Z44DidTocKghtknf674__LQ6z1ZuVgE
"""

import random
import pandas as pd
import time

card_vals = {'2':2 ,'3':3, '4':4, '5':5 ,'6':6, '7':7 ,'8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}
card_suits = ['d','h','c','s']
cardVals_list = list(card_vals.keys())
bankroll = 1000

# Random Card Generator
def genCard(dealt_cards):
  while True:
    card = random.choice(cardVals_list) + random.choice(card_suits)
    if card not in dealt_cards:
      return card

# Calculates Hand Value
def calc_hand_val(hand):
  hand_value = 0
  for card in hand:
    card_rank = card[:-1]
    hand_value += card_vals[card_rank]
  if 'A' in hand:
    if hand_value > 21:
      hand_value -= 10
  return hand_value

# Player Busts
def loss():
  global bankroll
  print('Player Loses')
  print('Bankroll: ', bankroll)

# Player Wins
def win(betAmnt):
  global bankroll
  winAmnt = betAmnt * 2
  bankroll += int(winAmnt)
  print('Player Wins:', int(betAmnt))
  print('Bankroll: ', int(bankroll))

# Player Pushes
def push(betAmnt):
  global bankroll
  bankroll += betAmnt
  print('Push')
  print('Bankroll: ', bankroll)


''''''''''''''''''''''''''''''''''''''''''


# Start Game
def startGame():
  global bankroll
  print('Welcome to Blackjack!')
  print('Bankroll:', bankroll)

  playerCards=[]
  dealerCards=[]
  playerHandVal = 0
  dealerHandVal = 0
  dealt_cards=[] # All cards that have been dealt

  betAmnt = int(input('How much would you like to bet? '))
  if betAmnt > bankroll:
    print('You do not have enough money to bet that amount.')
    return
  bankroll -= betAmnt
  time.sleep(1)

  # Generating Cards
  playerCard1 = genCard(dealt_cards)
  dealt_cards.append(playerCard1)
  playerCard2 = genCard(dealt_cards)
  dealt_cards.append(playerCard2)
  dealerCard1 = genCard(dealt_cards)
  dealt_cards.append(dealerCard1)
  dealerCard2 = genCard(dealt_cards)
  dealt_cards.append(dealerCard2)

  # Dealing cards
  playerCards.extend([playerCard1, playerCard2])
  dealerCards.extend([dealerCard1, dealerCard2])


  # Calculating Hand Value
  playerHandVal = calc_hand_val(playerCards)
  dealerHandVal = calc_hand_val(dealerCards)

  # Push (Both Dealer & Player Have Blackjack)
  if playerHandVal == 21 & dealerHandVal == 21:
    print("Player Cards: ", playerCards)
    print("Dealer Cards: ", dealerCards)
    time.sleep(1.5)
    print('Push')
    push(betAmnt)
    return

  # Player Gets Blackjack
  elif playerHandVal == 21:
    print("Player Cards: ", playerCards)
    print("Dealer Cards: ", dealerCards)
    time.sleep(1.5)
    print('Blackjack!')
    winAmnt = betAmnt * 2.5
    bankroll += int(winAmnt)
    print('Player Wins:', int(winAmnt))
    time.sleep(.5)
    print('Bankroll: ', int(bankroll))
    return

  # Dealer Gets Blackjack
  elif dealerHandVal == 21:
    print("Player Cards: ", playerCards)
    print("Dealer Cards: ", dealerCards)
    time.sleep(1.5)
    print('Dealer Has Blackjack')
    loss()
    return

  print("Player Cards: ", playerCards, '  |  Player Hand Value:', playerHandVal)
  print("Dealer Cards: ", ["?,", dealerCards[0]])
  time.sleep(2)

  # Player Chooses to hit or stay
  while playerHandVal < 21:
    player_action = input("Choose your action: Hit, Stay, or Double? (Enter 'h', 's' or 'd'): ").lower()


    # Code for if the player hits
    if player_action == 'h':
      print("Player chooses to Hit.")
      playerCard3 = genCard(dealt_cards)
      dealt_cards.append(playerCard3)
      playerCards.append(playerCard3)
      playerHandVal = calc_hand_val(playerCards)
      print("Player Cards: ", playerCards, '  |  Player Hand Value', playerHandVal)
      time.sleep(1.5)

      if playerHandVal > 21:
        print('Bust')
        loss()
        return
      elif playerHandVal == 21:
        print('Player Has 21')
        break

    # Code for if the player doubles
    elif player_action == 'd':
      print("Player chooses to Double.")
      playerCard3 = genCard(dealt_cards)
      dealt_cards.append(playerCard3)
      playerCards.append(playerCard3)
      playerHandVal = calc_hand_val(playerCards)
      bankroll -= betAmnt
      betAmnt *= 2  # Doubles bet
      time.sleep(1.5)
      break

    # Code for if the player stays
    elif player_action == 's':
      print("Player chooses to Stay.")
      break

    else:
      # Handle invalid input
      print("Invalid input. Please enter 'h', 's', or 'd'.")

  print('Players Final Hand:', playerCards, '  |  Player Hand Value', playerHandVal)
  print('Dealers Hand:', dealerCards, '  |  Dealer Hand Value', dealerHandVal)
  time.sleep(1.5)

  # Dealers Turn Logic
  while dealerHandVal < 17:
    dealerCard3 = genCard(dealt_cards)
    dealt_cards.append(dealerCard3)
    dealerCards.append(dealerCard3)
    dealerHandVal = calc_hand_val(dealerCards)

    print('Dealer Hits')
    print('Dealer Cards:', dealerCards, '  |  Dealer Hand Value', dealerHandVal)
    time.sleep(1.5)

    if dealerHandVal > 21:
      print('Dealer Busts')
      win(betAmnt)
      return

  if dealerHandVal > playerHandVal:
    loss()
  elif dealerHandVal < playerHandVal:
    win(betAmnt)
  else:
    push(betAmnt)

# Main game loop
while True:
  startGame()
  play_again = input("Play again? (y/n): ").lower()
  if play_again != 'y':
    break

