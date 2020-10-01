#check whether a string is a palindrome
def palCheck(name):
    if(name == name[::-1]):
        print("Its a palidrome")
    else:
        print("Not a palindrome")
name=input("Enter a word: ")
palCheck(name)           