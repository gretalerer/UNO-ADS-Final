class Node:  
  def __init__(self, value):
    self.value = value
    self.next = None


class Stack:

  def __init__(
    self
  ):  # Stack constructor. When we initialize the Stack, it is empty, so the top pointer is null (None)
    self.top = None

  def push( #Using the push algorithm has a time complexity of O(1) for a single element. Although when we push the full stack for example it could be O(n)
      self, value
  ):  # each value shall be "pushed" at the beginning of the linked list
    node = Node(value)  # Create a new Linked List Node
    node.next = self.top  # Link the new node with the head of the list, this is, the top of the stack
    self.top = node  # Make the new node become the top

  def pop(self): #Using the pop algorithm has a time complexity of O(1) for a single element. Although when we pop the full stack for example it could be O(n)
    if self.top is None:  # Base case to avoid Stack Underflows
      return None
    node = self.top  # get the node at the top
    self.top = node.next  # make top point to the next element in the list
    return node.value

  ## Time Complexity: O(1) for all as it just initializes variables 


