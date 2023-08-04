"""Hangman Game"""
print("Welcome to HANGMAN!")
import random
import time
x=("time year people way day man thing woman life child world school state family student group country problem hand part place case week company system program question work government number night point home water room mother area money story fact month lot right study book eye job word business issue side kind head house service friend father power hour game line end member law car city community name president team minute idea kid body information back parent face others level office door health person art war history party result change morning reason research girl guy moment air teacher force education").split()
word=random.choice(x)
print("\n ------\n|     |\n|     \n|     \n|     \n|     \n|     \n----------")
blanks2="__"
blanks3="___"
blanks4="____"
blanks5="_____"
blanks6="______"
blanks7="_______"
blanks8="________"
blanks9="_________"
blanks10="__________"
blanks11="___________"
if len(word)==2:
    length=blanks2
    print("Word length:", blanks2)
if len(word)==3:
    length=blanks3
    print("Word length:",blanks3)
if len(word)==4:
    length=blanks4
    print("Word length:",blanks4)
if len(word)==5:
    length=blanks5
    print("Word length:",blanks5)
if len(word)==6:
    length=blanks6
    print("Word length:",blanks6)
if len(word)==7:
    length=blanks7
    print("Word length:",blanks7)
if len(word)==8:
    length=blanks8
    print("Word length:",blanks8)
if len(word)==9:
    length=blanks9
    print("Word length:",blanks9)
if len(word)==10:
    length=blanks10
    print("Word length:",blanks10)
if len(word)==11:
    length=blanks11
    print("Word length:",blanks11)
print(len(word),"letters")
length=list(length)
count=0

while True:
    
    guess=input("Choose a letter or word:").lower() 
    if guess=="quit":
        quit()   
    guess_length=len(guess)
    word_length=len(word)
    if guess in word:
        if word[0]==guess:
            length[0]=guess
            print("".join(length))
        if word[1]==guess:
            length[1]=guess
            print("".join(length))
        if len(word)>2 and word[2]==guess:
            length[2]=guess
            print("".join(length))
        if len(word)>3 and word[3]==guess:
            length[3]=guess
            print("".join(length))
        if len(word)>4 and word[4]==guess:
            length[4]=guess
            print("".join(length))
        if len(word)>5 and word[5]==guess:
            length[5]=guess
            print("".join(length))
        if len(word)>6 and word[6]==guess:
            length[6]=guess
            print("".join(length))
        if len(word)>7 and word[7]==guess:
            length[7]=guess
            print("".join(length))
        if len(word)>8 and word[8]==guess:
            length[8]=guess
            print("".join(length))
        if len(word)>9 and word[9]==guess:
            length[9]=guess
            print("".join(length))
        if len(word)>10 and word[10]==guess:
            length[10]=guess
            print("".join(length))
        if len(word)>11 and word[11]==guess:
            length[11]=guess
            print("".join(length))
    hangman0="------\n|     |\n|     \n|     \n|     \n|     \n|     \n----------"
    hangman1="------\n|     |\n|     o    \n|     \n|     \n|     \n|     \n----------"
    hangman2="------\n|     |\n|     o    \n|     |     \n|          \n|     \n|     \n----------"
    hangman3="------\n|     |\n|     o    \n|     |     \n|     |     \n|     \n|     \n----------"
    hangman4="------\n|     |\n|     o    \n|    /|     \n|     |     \n|     \n|     \n----------"
    hangman5="------\n|     |\n|     o    \n|    /|\     \n|     |     \n|     \n|     \n----------"
    hangman6="------\n|     |\n|     o    \n|    /|\     \n|     |     \n|    /     \n|     \n----------"
    hangman7="------\n|     |\n|     o    \n|    /|\     \n|     |     \n|    / \     \n|     \n----------"
    # hangman8=
    # hangman9=
    print(length)
    if guess_length>1:
        if guess in word:
            print("Yay! You won! The word was:",word)
            time.sleep(20)
            quit()
        else:
            count=count+1
            print("nope")
            if count==1:
                print(hangman1)
            elif count==2:
                print(hangman2)
            elif count==3:
                print(hangman3)
            elif count==4:
                print(hangman4)
            elif count==5:
                print(hangman5)
            elif count==6:
                print(hangman6)
            elif count==7:
                print(hangman7)
                print("You lose!!! The word was:",word)
                time.sleep(20)
                quit()
                
    else:
        if guess in word:
            
                
            print("Yes, that letter is in the word!")

        else:
            print("Your guess is not in the word.")
            
            count=count+1
            if count==1:
                print(hangman1)
            elif count==2:
                print(hangman2)
            elif count==3:
                print(hangman3)
            elif count==4:
                print(hangman4)
            elif count==5:
                print(hangman5)
            elif count==6:
                print(hangman6)
            elif count==7:
                print(hangman7)
                print("You lose!!! The word was:",word)
                time.sleep(20)
                quit()