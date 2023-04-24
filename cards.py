import random

class Deck:

  def __init__(self):
    self.cards = []
    self.build()

  def build(self): #Here we create the arrays we will use to build the card and deck
    colours = ["Red", "Green", "Yellow", "Blue"]
    values = [
      '1', '2', '3', '4', '5', '6', '7', '8', '9', "+2", 'skip'
    ]
    wilds = ['add 4', 'change color']
    
    for colour in colours: #We start creating basic cards
      if colour == "Blue":
        if values == '1':
          continue 
      for number in values:
        self.cards.append(f"{colour} {number}")

    for i in range(4): #We create the wildcards
      self.cards.append(f'Wild {wilds[0]}')
      self.cards.append(f'Wild {wilds[1]}')

  ## Time Complexity: O(m*n) as it iterates through 2 arrays to create the cards 

  def show(self): #Function to see the cards
    for card in self.cards:
      print(card)

  ## Time Complexity: O(n) as it iterates through 1 array to print the cards 


  def shuffle(self): #function to shuffle the cards
    for i in range(len(self.cards) - 1, 0, -1):
      r = random.randint(0, i + 1)
      self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

  ## Time Complexity: O(n) as it iterates through 1 array to shuffle the cards 


  