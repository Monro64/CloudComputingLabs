#fINAL VERSION.
word = (input(" Please enter the string you want \n")) #Modified to take in input
word = word.lower() #Removed case sensitivity, works for any and all strings.
wordRev = word[::-1] #reverses original string, stores in new variable
#Counter removed, no need for it.

if (word == wordRev): #Compares current string to reversed one. Will work no matter what, regardless of characters
  #or spaces present in the input string.
  {
    print ("True")
  }
else:
  {
    print ("False")
  }
