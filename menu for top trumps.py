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




    
