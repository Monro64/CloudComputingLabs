#Second version of code, does not work. Wanted to try shorter comparison.
word = "Oxo" # first test for predefined word
wordRev = word[::-1] #reverses original string, stores in new variable
#Counter removed, no need for it.

if (word == wordRev): #This should work, considering if it is a palindrome, they will simply be identical.
  {
    print "True"
  }

else: #It did not.
  {
    print "False"
  }