#/usr/bin/python
# -*- coding: utf-8 -*-
# collaborated with zy2339 and jn2770
# this code is used for advanced swe now 

import random

class Card(object):  
    
    def __init__(self, suit, value):
        self.suit = suit
        self.rank = value         

    def __str__(self):
        return "{} {}".format(self.suit, self.rank) 

    def value(self, total):
        if self.rank == "J" or self.rank == "Q" or self.rank == "K":
          total += 10
        elif self.rank == "A":
          if 11 + total > 21:
            total += 1
          else: 
            total += 11
        else: 
          total += int(self.rank)
        return total


def make_deck():
    suits = ['♠','♣','♦','♥']
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    some_list = list()
    for suit in suits:
      for rank in ranks:
        card = Card(suit, rank) 
        some_list.append(card)
    random.shuffle(some_list)
    for card in some_list: 
      print(card.__str__())
    return some_list

def main():
    deck = make_deck()
    card_idx = 0
    player_score = 0
    dealer_score = 0
    exit = False

    while (card_idx < len(deck) and exit == False):
      print("You drew " + deck[card_idx].__str__())
      player_score = deck[card_idx].value(player_score)
      print("sum: " + player_score.__str__())
      card_idx += 1
      if (player_score == 21):
        print("You win")
        exit = True
      elif (player_score > 21):
        print("I win")
        exit = True
      else:
        answer = input("Do you want another card? (y/n)") 
        if (answer == "y"):
          continue
        elif (answer == "n"): 
          print("My turn.") 
          while (dealer_score < 17):
            print("I drew " + deck[card_idx].__str__())
            dealer_score = deck[card_idx].value(dealer_score)
            print("My sum: " + dealer_score.__str__())
            card_idx += 1

          if (dealer_score > 21 and player_score > dealer_score):
            print("You win")
            exit = True
          elif (player_score == dealer_score):
            print("It is tie")
            exit = True
          else: 
            print("I win")
            exit = True

if __name__ == "__main__":
    main()
