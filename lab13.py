def explain(): #explains game
  showInformation("Welcome, in this game there is a story but you will replace the some words unknowingly when prompted and read the message out loud have fun!")


#------------------------------------------------------------------------------------------
def userInput():  #function to store user info

  userName = []
  print "Enter your name: "
  name = raw_input()
  userName.append(name)
  
  
  #creates a list that contains some context for the word to be entered:
  messageList = ["Location: ","Verb: ","Day of the week: ","Age: ","First name: ",
  "Last name: ","Acivity: ","Plural Noun: ","Emotion: ","Noun: ","Noun: ","Last Name: ","noun: "
  ,"First name: ","noun: ","plural noun: "," noun: ","location: ","Last name: ","subject: " ]  
  
  myList = [] #empty list to add all the words the user inserts
  for x in range(len(messageList)): # trasverses the list to print one at a time from messageList
    print messageList[x]
    print "Enter a word you would like to use" 
    for i in range(1): #nested loop to append the list to store the words the user inserted
      words = raw_input()
      myList.append(words) # add input to the list
      print(myList)
    
  #prints out the whole story passing the stored values of the list provided by the user  
  print myList[0] + "-Describing the utter lack of ambition as " + myList[1] + ", sources confirmed"
  print myList[2] + " that local" + myList[3] + " -year-old " + myList[4] + " " + myList[5] + " has been wasting his life playing"
  print myList[6] + " when there's a whole world of other " + myList[7] + " out there. It's really" 
  print myList[8]+" to see a guy like that spedning eight hours a day holed up with his" + myList[9]
  print " when he could be staring at his phone or his " + myList[10] +" instea, said a source close to"
  print myList[11] + " expressing bewilderment over why anyone would sing that much time into"
  print myList[12] +" when the world has so many streaming services, YouTube videos,social" 
  print " media feed to offer, and they're all within arm's reach." + myList[13] +" is always on the couch"
  print " holding "+ myList[14] +" ,even though he could be holding one of four or five different"
  print myList[15] +" instead. He hardly ever powers up his "+ myList[16]+ " anymore, and I"
  print "honestly don't remeber the last time he went outside to go to a "+ myList[17] + ".He's really"
  print "missing out. The source also confirmed that it has probably been years since" + myList[18] +" last"
  print "read a book on " + myList[19]

  print "\nCongratulation you made it through you win " + userName[0] + "!!"



#------------------------------------------------------------------------------------------
#function to play the game 
def playGame():        #plays the game for the user
 
 explain()
 userInput() 
 

  
   
 
