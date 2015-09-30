#Third test, a glaringly obvious syntax error turned out to be my downfall.
word = "oxo" # first test for predefined word
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
