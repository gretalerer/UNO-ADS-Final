from cards import Deck
from allocate_cards import allocate_cards
from sorting_algos import quicksort_mid
from games2 import draw_card
from games2 import canPlay
from games2 import shuffling
from games2 import plus_2
from games2 import add_4
from games2 import change_color
from games2 import rules
from priority import *
from test import Test
import os 
from stack import *


def main():

  #creating a deck instance + shuffling it 
  deck = Deck() 
  deck.build()
  deck.shuffle()

  print('Welcome to UNO!')

  #starting the game with the desired amount of players
  numPlayers = int(input("How many players? "))
  if numPlayers > 5 or numPlayers < 2:
    numPlayers = int(input("How many players? (2-5) "))

  #giving the cards to the number of players
  players = allocate_cards(numPlayers, deck)

  access = True #boolean access: to keep the game running
  middle_deck = Stack()
  middle_deck.push("Blue 1") #placing the first card on the middle deck
  curMid = middle_deck.pop() 



  rules()

  any = input("Press anything to start the game.")
  os.system('clear')

  if any:

    playing = True #playing is a boolean that controls when each player is done playing its turn
    #os.system('clear')
    while (access):
      for i in range(len(players)):
        
        if len(players[i]) != 0:  
          if len(players[i]) == 1:
            print("Player ", i+1," says uno!!")

            
          if 'skip' in curMid: #if the middle card is skip, then the player has to be skipped
            curMid = curMid.split()
            curcol = curMid[0]
            curMid = curcol + " Any number"
            continue #that's why we skip this iteration of the loop by using continue

          players[i] = quicksort_mid(players[i]) #quicksorting each subarray
          print(f'Current player: {i + 1}') 
          print(' ')
          print(f'The cards of player {i + 1} are: {players[i]}')
          print()
          print(f'Current middle card: {curMid}')

          print(' ')
          Test(players[i], curMid)
          print()

          y = int(
            input('Please enter the position of your card or 50 to draw a card: ')) #The user inserts his hand
          playing = True #Once the player inserts its card, the game starts

          while playing == True:

            if (y == 50): #condition for the player to draw cards
              deck, players, y = draw_card(deck, players, i, curMid)

            else:
              while y > len(players[i]): #to prevent an error happening when you insert a wrong number
                y = int(
                  input(
                    'Please enter the correct position of your card or 50  to draw a card: '
                  ))
                if (y == 50):
                  deck, players, y = draw_card(deck, players, i, curMid)
              thrownCard = players[i][y]

              if canPlay(curMid, thrownCard): #canPlay is a boolean function that checks whether the card you are inserting is adequate for the current middle card
                print(f'The card you just threw is {thrownCard}')
                middle_deck.push(thrownCard) #middle deck add the card that was just thrown
                #scenario 1:
                if 'change color' in thrownCard:
                  middle_deck, players = change_color(thrownCard, y, i,
                                                      middle_deck, players)

                #scenario 2: 
                elif 'add 4' in thrownCard:
                  players, middle_deck, deck = add_4(players, middle_deck, y,
                                                     i, deck)

                #scenario 3:
                elif '+2' in thrownCard:
                  players, deck = plus_2(i, y, players, deck)

                #scenario 4:
                elif 'skip' in thrownCard:
                  print(f'Next player will be skipped!')
                  players[i].pop(y)

                #scenario 5:
                else:
                  players[i].pop(y) #if the card has no 'effect', then we just remove it from the players array. 

                print(' ')
                curMid = middle_deck.pop()  #replace the current middle card with the new middle card.
                os.system('clear')

                playing = False  #This means that the player has finished their round. 

              else: #scenario for when canPlay is False, which means that the card inserted was not correct. 
                print(' ')
                print(
                  f"The card you threw cannot be played here. Remember the card in the middle is: {curMid}"
                )
                print()
                y = int(
                  input(
                    "Please enter the position of your card or 50 to draw a card: "
         
                  
                  ))
                
        if len(players[i]) ==  0: #condition for when someone wins the game: the array is empty. 
          print("Player ", i + 1, " has won the game!!")
          access = False
          print("Game has ended!!")
          break
        
        if len(players[i]) == 0:
          break

  # *******************
main()


