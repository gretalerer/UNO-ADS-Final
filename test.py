import heapq as hq


def Test(player_arr, middle_card):
  priority_list = [] #Here we create the list of possible outcomes
  for card in player_arr:
    if "add 4" in card:
      priority_list.append((1, card)) #Priority 1 for add 4
    if "change color" in card:
      priority_list.append((2, card))#Priority 2 for change color
  c = middle_card.split()#Here I split the middle card to assess two parts: the color and the number or second part of the array


  if c[0] == "Green":
    for i in player_arr:
      if "Green" in i:
        if "skip" in i:
          priority_list.append((3, i)) #In all colors, we will give it a priority 3 for skips
        if "+2" in i:
          priority_list.append((4, i))#In all colors, we will give it a priority 4 for add 2
        if "+2" not in i and "skip" not in i:
          priority_list.append((5, i))#In all colors, we will give it a priority 5 for being the same color
      else:#Here I check to be sure its not a special card
        if c[1] in i and "Wild add" not in middle_card and "Green +2" not in middle_card:
          priority_list.append((6, i))#In all colors, we will give it a priority 6 for being the same number
                               
      
  if c[0] == "Yellow":
    for i in player_arr:
      if "Yellow" in i:
        if "skip" in i:
          priority_list.append((3, i))#In all colors, we will give it a priority 3 for skips
        if "+2" in i:
          priority_list.append((4, i))#In all colors, we will give it a priority 4 for add 2
        if "+2" not in i and "skip" not in i:
          priority_list.append((5, i))#In all colors, we will give it a priority 5 for being the same color
      else:#Here I check to be sure its not a special card
        if c[1] in i and "Wild add" not in middle_card and "Red +2" not in middle_card:
          priority_list.append((6, i))#In all colors, we will give it a priority 6 for being the same number
                               
                           
      

  if c[0] == "Red":
    for i in player_arr:
      if "Red" in i:
        if "skip" in i:
          priority_list.append((3, i))#In all colors, we will give it a priority 3 for skips
        if "+2" in i:
          priority_list.append((4, i))#In all colors, we will give it a priority 4 for add 2
        if "+2" not in i and "skip" not in i:
          priority_list.append((5, i))#In all colors, we will give it a priority 5 for being the same color
      else:#Here I check to be sure its not a special card
        if c[1] in i and "Wild add" not in middle_card and "Red +2" not in middle_card:
          priority_list.append((6, i))#In all colors, we will give it a priority 6 for being the same number
                               
      

  if c[0] == "Blue":
    for i in player_arr: 
      if "Blue" in i:
        if "skip" in i:
          priority_list.append((3, i))#In all colors, we will give it a priority 3 for skips
        if "+2" in i:
          priority_list.append((4, i))#In all colors, we will give it a priority 4 for add 2
        if "+2" not in i and "skip" not in i:
          priority_list.append((5, i))#In all colors, we will give it a priority 5 for being the same color
      else:#Here I check to be sure its not a special card
        if c[1] in i and "Wild add" not in middle_card and "Red +2" not in middle_card:
          priority_list.append((6, i))#In all colors, we will give it a priority 6 for being the same number
                               


  hq.heapify(priority_list)#Here, we make the list go into priority where 1 would be the first and 6 would be the last
  ## Furthermore, the runtime of the heapify function here is O(ln(n)) for an average, and O(1) for the best time.
  print("The system's recommended card is :")
  
  for i in priority_list:
    print(i[1])#Here I print the most important recommendation our system gives us
    break

## Time Complexity: O(n * m) as it iterates through 1 array to perform all the operations. 