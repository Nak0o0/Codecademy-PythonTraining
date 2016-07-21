"""Pig Latin is a language game, where you move the first letter of the word to the end and add "ay." 
So "Python" becomes "ythonpay." To write a Pig Latin translator in Python, here are the steps we'll need to take:

    1. Ask the user to input a word in English.
    2. Make sure the user entered a valid word.
    3. Convert the word from English to Pig Latin.
    4. Display the translation result. """

word=input("Please enter a word!")
letters=0
temp=0

if word.isalpha():
    letters=list(word) 
    temp = letters.pop(0)
    letters.insert(len(letters), temp + "ay")
    print( ''.join(letters) )
else :
    print ("That\'s not a valid word")
