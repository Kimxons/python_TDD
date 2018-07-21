# A palindrome is a word that is read the same from front-to-back and from back-to-front.
# implemented by traversing the given word or phrase forwards and backwards
# to check whether it is the same
# using a stack D.S to find palindromes

#defining a class -stack class
class Stack:
    def __init__(self):
        self.items=[]

    #function to check whether the stack is empty
    def isEmpty(self):
        return self.items==[]

    #function to insert items into the stack
    def push(self,data):
        self.items.append(data)

    #function to check the size of the stack
    def size(self):
        return len(self.items)

    #function list the stack items
    def show(self):
        print (self.items)

    #function to return the value of the 'top item' without removing it
    def peek(self):
        return self.items[len(self.items)-1]

    #function remove the top item of the stack
    def pop(self):
        assert not self.isEmpty()
        return self.items.pop() #return the popped item

#to request for the input from the user
word=input("Enter a word: ")
s=Stack()

for k in word:
 s.push(k)

list = ""
while not s.isEmpty():
   list += s.pop()

if(list == word):
    print(word,"is a palindrome")
else:
    print(word,"is not a palindrome")
