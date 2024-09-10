print("=======================WELCOME TO MY QUIZ GAME=======================")
playing = input("DO YOU WANT TO PLAY?  ")
if playing.lower() != 'yes':
    quit()
    
print("okay! lets play:😎")
score = 0
answer = input("What is C.P.U?  ")
if answer.lower() == "central processing unit":
    print("correct!💯")
    score += 1
else:
    print("incorrect!😪")
    
    
answer = input("What is a G U I?  ")
if answer.lower() == "graphical user interface":
    print("correct!💯")
    score += 1
else:
    print("incorrect!😪")
    
answer = input("What is UI?  ")
if answer.lower() == "user interface":
    print("correct!💯")
    score += 1
else:
    print("incorrect!😪")
    
answer = input("What does RAM stands for?  ")
if answer.lower() == "random acces memory":
    print("correct!💯")
    score += 1
else:
    print("incorrect!😪")
    
    
print("you got " + str(score) + "  " + "questions correct!")
print("you have" + str((score / 4) * 100) + "%.")    