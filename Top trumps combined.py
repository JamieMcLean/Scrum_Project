import random
import time

main():

    def userdeck(deck):
        for i in range (0,10):
            userdeckTemp = random.choice(deck)
            userDeck.append(userdeckTemp)
        print ('\n','your deck contains: ')
        for i in userDeck:
            print(i,'\n')

        def aideck(deck):
      for i in range(0,10):
        aideckTemp = random.choice(deck)
        aiDeck.append(aideckTemp)

    def my_shuffle():
        array1 = ['a','b','c','d','e','f']
        random.shuffle(array)
        print(array)
        return array

    def gameMenu():
    ans=True
    while ans:
        print(" 1.Play the Game 2.Instructions  3.Exit/Quit")
        
        ans=input("What would you like to do? ")
        if ans=="1":
          name = input("\n What is your name? ")
          print("Hello ", name, ". Let's play Top Trumps!")
          playGame()
        elif ans=="2":
          print("\n Okay then. ")
          instructions()
          askQuestion = input("do you want to play the game now?")
          if askQuestion == 'yes':
              print("Okay. Let's play!")
              playGame()
        elif ans=="3":
          print("\n Goodbye") 
          ans = False
        else:
            print("\n Please Enter an Option Shown")

    def instructions():
        listInstruction = print(""" \n Here are the Instructions for the game:
                  1.You are given five top trumps, as does the computer
                  2.List the category you want to pick
                  3.If the category you picked has more points than the computer's,
                  then you get a point.
                  4.If you have the highest number after five rounds, then you win!
                  """)
    gameMenu()

    Game = True

    #in between the brackets you will have to place 4 things. of varying levels and replace
    #the letters with ppl

    # e.g q = q(name),q(power),q(agility),q(magic)
    q= ('q','10','29','20') 
    w= ('w','11','28','21')
    e= ('e','12','27','22')
    r= ('r','13','26','23')
    t= ('t','14','25','24')
    y= ('y','15','24','25')
    u= ('u','16','22','26')
    i= ('i','17','23','27')
    o= ('o','18','21','28')
    p= ('p','19','20','29')
    a= ('a','20','19','19')
    s= ('s','21','18','18')
    d= ('d','22','17','17')
    f= ('f','23','16','16')
    g= ('g','24','15','15')
    h= ('h','25','14','14')
    j= ('j','26','13','13')
    k= ('k','27','12','12')
    l= ('l','28','11','11')
    z= ('z','29','10','10')
    deck = (q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z)

    #this is the game
    def game(deck):
        userDeck = []
        aiDeck = []
        card = 1
