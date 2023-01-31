class Stack:
  def __init__(self):
    # Initialize an empty list to store the elements of the stack
    self.stack = []
  
  def push(self, element):
    # Add an element to the top of the stack
    self.stack.append(element)
  
  def pop(self):
    # Check for stack size before popping
    if self.size() == 0:
      raise IndexError("Stack is empty")

    # Remove and return the element at the top of the stack
    return self.stack.pop()
  
  def peek(self):
    # Return the element at the top of the stack without removing it
    return self.stack[-1]
  
  def is_empty(self):
    # Return True if the stack is empty, False otherwise
    return not self.stack
  
  def size(self):
    # Return the number of elements in the stack
    return len(self.stack)

# Create a new stack object
stack = Stack()

# Test the stack methods
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())  # 3
print(stack.pop())  # 3
print(stack.pop())  # 2
print(stack.pop())  # 1
print(stack.is_empty())  # True
print(stack.size())  # 0

