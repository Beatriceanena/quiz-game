print('Hello, Welcome to the Javascript IQ skill Test ')
question1= input('Are you currently doing Javascript? ').lower()
if question1 != "yes":
    quit()
else:
    print("Okay continue")
    score=0

answer = input('What is the javascript search engine for chrome called? ').lower()
if answer == "v8":
    print("Correct")
    score+=1
else:
    print("Incorrect")
  
answer =input("How are constant variables declared in javascript? ").lower()
if answer == "const":
    print("Correct")
    score+=1
else:
    print("Incorrect")
   
answer =input("How are variables declared in javascript? ").lower()
if answer == "let":
    print("Correct")
    score+=1
else:
    print("Incorrect")

answer =input("Which javascript framework is used in backend development ").lower()
if answer == "node.js":
    print("correct")
    score+=1
else:
    print("Incorrect")    

print("You scored" +  str((score/4)*100) +"%")
if score == 25:
    print("You are under skilled")
if score == 50:
    print("You are semi skilled")
if score ==75:
    print("You are a genius ")   
else:
    print("You are not skilled")
      






    