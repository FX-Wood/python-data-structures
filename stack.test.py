from stack import Stack

print(Stack)

stack = Stack()

# add two ints to the stack
stack.push(5)
stack.push(13)

print( stack.peek() ) # prints 5

stack.pop() # returns 5

print( stack.peek() ) # prints 13

# these lines will empty the stack and return an index error
# stack.pop()
# print( stack.peek() )