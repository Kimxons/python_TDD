class Stack:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def push(self,data):
        self.items.append(data)

    def size(self):
        return len(self.items)

    def show(self):
        print (self.items)

    def peek(self):
        return self.items[len(self.items)-1]

    def pop(self):
        assert not self.isEmpty()
        return self.items.pop()

word=input("Enter a word: ")
s=Stack()

for k in word:
 s.push(k)

list = []
while not s.isEmpty():
   list += s.pop()

if(list == word):
    print(word,"is a palindrome")
else:
    print(word,"is not a palindrome")