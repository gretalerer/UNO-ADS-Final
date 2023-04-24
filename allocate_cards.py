from cards import *

def allocate_cards(numPlayers, deck): #function to generate our multi dimensional array where we store all players. 
  arr = [[0 for _ in range(7)] for _ in range(numPlayers)]
  for i in range(len(arr)):
    for j in range(7):
      arr[i][j] = deck.cards.pop()

  return arr 

## Time complexity : O(m*n) as it iterates through each value in a 3-dimensional array



