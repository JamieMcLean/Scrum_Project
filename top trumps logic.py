import random

def game('''add what you need to in here'''):
#these are the stats of the cards
    userPower = userCard[1]
    userAgility = userCard[2]
    userMagic = userCard[3]
    aiPower = aiCard[1]
    aiAgility = aiCard[2]
    aiMagic = aiCard[3]

#these are the ai points and the user points
    userScore = 0
    aiScore = 0
    number = 0
#this while loop make sure you play again. and the end will happen once you get the ai's cards.
    endGame = False
    while endGame == False:
        print('Your card is: ',userCard)
        userstatTemp = input('which stat do you wish to compare? Power, Agility or Magic?')
        if userstatTemp == 'power':
            print('your card is: ',userCard)
            if int(userPower) > int(aiPower):
                print('You Won! you have a higher power stat than the computer!','\n')
                print('your stat was ',userPower,'while his was ',aiPower,'!')
                userScore = userScore + 1
                
            elif int(userPower) < int(aiPower):
                print('Oh no!!! You lost...the computer had a higher power stat than you!','\n')
                print('your stat was ',userPower,'while his was ',aiPower,'!')
                aiScore = aiScore + 1
                
            else:
                print('Uh Oh...you and the computer seem to have come to a draw!','\n')
                print('There is only one thing to do! continue. draws do not count as points.')
            card = card + 1
            if userScore != 10:
                print('\n')
            else:
                print('OhMyGosh You won!!!!!!!!!!')
                endGame = True
            if aiScore != 10:
                print ('\n')
            else:
                print('I\'m so sorry about this but you have lost! You have been defeated by the AI!!!!')
                endGame = True
                      
        elif userstatTemp == 'agility':
            print('your card is: ',userCard)
            if int(userAgility) > int(aiAgility):
                print('You Won! you have a higher power stat than the computer!','\n')
                print('your stat was ',userAgility,'while his was ',aiAgility,'!')
                userScore = userScore + 1
                
            elif int(userAgility) < int(aiAgility):
                print('Oh no!!! You lost...the computer had a higher power stat than you!','\n')
                print('your stat was ',userAgility,'while his was ',aiAgility,'!')
                aiScore = aiScore + 1
                
            else:
                print('Uh Oh...you and the computer seem to have come to a draw!','\n')
                print('There is only one thing to do! continue. draws do not count as points.')
            card = card + 1
            if userScore != 10:
                print('\n')
            else:
                print('OhMyGosh You won!!!!!!!!!!')
                endGame = True
            if aiScore != 10:
                print ('\n')
            else:
                print('I\'m so sorry about this but you have lost! You have been defeated by the AI!!!!')
                endGame = True
            
        elif userstatTemp == 'magic':
            print('your card is: ',userCard)
            if int(userMagic) > int(aiMagic):
                print('You Won! you have a higher power stat than the computer!','\n')
                print('your stat was ',userMagic,'while his was ',aiMagic,'!')
                userScore = userScore + 1
                
            elif int(userMagic) < int(aiMagic):
                print('Oh no!!! You lost...the computer had a higher power stat than you!','\n')
                print('your stat was ',userMagic,'while his was ',aiMagic,'!')
                aiScore = aiScore + 1
                
            else:
                print('Uh Oh...you and the computer seem to have come to a draw!','\n')
                print('There is only one thing to do! continue. draws do not count as points.')
            card = card + 1
            if userScore != 10:
                print('\n')
            else:
                print('OhMyGosh You won!!!!!!!!!!')
                endGame = True
            if aiScore != 10:
                print ('\n')
            else:
                print('I\'m so sorry about this but you have lost! You have been defeated by the AI!!!!')
                endGame = True
        else:
            print('WHO SAID YOU COULD PICK THAT! try again pls')
  game('''Also add what you need in here''')
