from cards import *
from sorting_algos import *
from test import *
from stack import *

def draw_card(deck, players,i, curMid): #function to draw cards
  a = deck.cards.pop() #remove the top card from the deck
  players[i].append(a) #append that card to the player drawing it
  players[i] = quicksort_mid(players[i]) #re-sorting the array
  print()
  print('Player ', i + 1, " now has: ")
  print(players[i])
  print()
  print(f'Current card: {curMid}')
  print()
  Test(players[i], curMid)
  print()
  y = int(input("Please enter the position of your card or 50 to draw a card: ")) #now is the time to either draw a card again or toss one
  print()
  return deck, players, y
  
#The time complexity for draw_card will be O(1), because everytime you draw a card, you only take 1 from the top.(The card that is popped)

#karim we could tilite this if u want
def canPlay(curMid, card): #this is the function to check whether the card being player is correct.

  curMid = curMid.split()
  curCol = curMid[0]
  curVal = curMid[1]

  #we are checking that the card drawn is suitable for the top card in the middle_deck
  
  if 'Wild' in card:
    return True
  elif (curCol in card) or (curVal in card): 
    return True
  return False

# Average run time complexity will be O(n) because you are going through the string card to check whether certain substrings are found there. 

def shuffling(deck):
  deck.shuffle()
  return deck

  
def change_color(thrownCard, y, i, middle_deck, players): #function to change color
  middle_deck.push(thrownCard) #add the thrown card into the middle_deck
  players[i].pop(y) #remove the card from the array of the player
  colors = ["Red", 'Yellow', 'Blue', 'Green']
  new_c = input("Enter the new color you want to use: ") #user enters the new color
  if new_c in colors: #check whether the color has been written correctly, otherwise you will be asked again.
    arr_card = new_c + " " + "Any number"
    middle_deck.push(arr_card)
  while new_c not in colors:
    new_c = input("Enter the new color you want to use with the first letter in caps:")
  if players is None: 
    print( f"Player {i+1} has just won the game!")
    print()
    print('THANK YOU FOR PLAYING UNO!!')
    quit()
  return middle_deck, players

## runtime complexity is: O(n) because you have to go through the elements of the array "colors" to check if what the user inserted is there. The best case would be O(1) where the card has the first element of the array 
  
def add_4(players, middle_deck, y, i, deck): #function to add 4
  removed_part = players[i][y]
  middle_deck.push(removed_part)
  players[i].pop(y)
 
  if i == len(players) - 1: #has to do with whether you are the last player or not.
    for j in range(4):
      a = deck.cards.pop()
      players[i - len(players) + 1].append(a)
  if i != len(players) - 1:
    for j in range(4):
      a = deck.cards.pop()
      players[i + 1].append(a)

  out = input("What color would you like to change to (Please write the first letter with caps)? ")  #choose color
  colors = ["Red", 'Yellow', 'Blue', 'Green']
  while out not in colors:
    out = input("Enter the new color you want to use with the first letter in caps:")
  card = out + " Any Number" #current middle card will now be the chosen color. 
  
  middle_deck.push(card)
  if players is None: 
    print( f"Player {i+1} has just won the game!")
    print()
    print('THANK YOU FOR PLAYING UNO!!')
    quit()
  return players, middle_deck, deck

## runtime complexity is: O(n) because you have to go through the elements of the array "colors" to check if what the user inserted is there. The best case would be O(1) where the card has the first element of the array.
  
    
    
def plus_2(i, y, players, deck): #draw 2 cards
  if i == len(players) - 1: #same as in +4: has to do with whether the player playing is the last one in the array or not. 
    if i == len(players) - 1:
      for j in range(2):
        a = deck.cards.pop()
        players[i - len(players) + 1].append(a)
  if i != len(players) - 1:
    for j in range(2):
      a = deck.cards.pop()
      players[i + 1].append(a)
  players[i].pop(y)
  if players is None: 
    print( f"Player {i+1} has just won the game!")
    print()
    print('THANK YOU FOR PLAYING UNO!!')
    quit()
  return players, deck

## Runtime complexity best and average case scenario is O(1) because you just have to append two cards to the player which is asymptotically equivalent to O(1)
  
def rules(): #function displaying the rules of the game.
  print('These are the UNO rules: ')
  print()
  print('1 - A wild card can be thrown at any moment. ')
  print()
  print('2 - If you are not throwing a wild card you have to match EITHER the color of the current middle card OR the number of the current middle card.')
  print()
  print('3 - The first person to run out of cards wins!')
  print()
  print('4 - After the first player wins, everyone gets an extra chance to also win!')
  print()
  print('5 - Good luck to all players!')
  print()
  print('6 - If you won but a player adds a card to your hand, you will go back to the game. ')
  print()

## Runtime complexity best and average case scenario is O(1).



