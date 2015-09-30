#fINAL VERSION.
word = (input(" Please enter the string you want \n")) #Modified to take in input
word = word.lower() #Removed case sensitivity, works for any and all strings.
wordRev = word[::-1] #reverses original string, stores in new variable
#Counter removed, no need for it.

if (word == wordRev): #This should work, considering if it is a palindrome, they will simply be identical.
  {
    print ("True")
  }
else: #It worked somewhat. Case handling to be added in final version
  {
    print ("False")
  }
