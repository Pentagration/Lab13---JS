#STUDENTS: Jason Pettit, Sergio Quiroz
#CST205-40_SP19
#Lab 13 - Madlib

def madLib():
  string = ('CRANSTON, RI Describing the utter lack of ambition as \"such a shame,\" '
  'sources confirmed Monday that local 27-year-old Andrew Maslia has been wasting his '
  'life playing video games when there\'s a whole world of other screens out there. ' 
  '\"It\'s really sad to see a guy like that spending eight hours a day holed up with ' 
  'his PS4 when he could be staring at his phone or his iPad instead,\" said a source ' 
  'close to Maslia, expressing bewilderment over why anyone would sink that much time '
  'into video games when the world has so many streaming services, YouTube videos, '
  'and social media feeds to offer, and they\'re all within arm\'s reach. \"Andrew '
  'is always on the couch holding a game controller, even though he could be holding ' 
  'one of four or five different remote controls instead. He hardly ever powers up his ' 
  'laptop anymore, and I honestly don\'t remember the last time he went outside to '
  'go to a movie theater. He\'s really missing out.\" The source also confirmed that '
  'it has probably been years since Maslia last read a book on his Kindle.')
  
  words = {"city":"CRANSTON,RI",
            "verb":"such a shame", 
            "dayOfWeek":"Monday", 
            "age":"27",
            "firstName":"Andrew",
            "lastName":"Maslia",
            "activity":"video games",
            "pluralNoun1":"video games",
            "emotion":"sad",
            "noun1":"PS4",
            "noun2":"iPad",
            "noun3":"video games",
            "noun4":"game controller",
            "pluralNoun2":"remote controls",
            "noun5":"laptop",
            "location":"movie theater",
            "subject":"his Kindle"}
  
  print words
  value = words.values()
  key = words.keys()
  
  #finds the matches to the dictionary values
  #in the string and replaces those sub-strings
  #with the value of the dictionary key
  #later we'll overwrite the keys with the user Input
  for x in range(0,len(value)):
    newString = string.replace(value[x],key[x])
    string = newString
  
  #request user input, and change the values
  #in the dictionary to the user input            
  for y in range(0,len(key)):
    userInput = requestString(key[y])
    words[key[y]] = userInput
  
  #overwrite values with user input values
  value = words.values()
  
  #find the keys in the string and overwrite
  #with the values
  for z in range(0,len(value)):
    newString = string.replace(key[z],value[z])
    string = newString
  
  print string