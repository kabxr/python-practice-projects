import random, sys

print('ROCK, PAPER, SCISSORS')

#setting init variables
win = 0
loss = 0
tie = 0
botChoices = ['r','p','s']

#main game loop
while True:
  print(f"{win} Wins, {loss} Losses, {tie} Ties")
  print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
  randNum = random.randint(0,2)
  botInput = botChoices[randNum]
  playerInput = input()
  if playerInput == 'q':
    sys.exit()

  if playerInput not in ['r','p','s','q']:
    print("Invalid input, please try again :)")
  else:
    if playerInput == 'r' and botInput == 'p':
      loss +=1
      print('Rock Versus Paper!')
      print('You lose')  
    elif playerInput == 'r' and botInput == 's':
      win += 1
      print('Rock Versus Scissors')
      print('You win!')
    elif playerInput == 'p' and botInput == 's':
      loss += 1
      print('Paper Versus Scissors')
      print('You lose!')
    elif playerInput == 'p' and botInput == 'r':
      win += 1
      print('Paper Versus Rock')
      print('You win!')
    elif playerInput == 's' and botInput == 'p':
      win += 1
      print('Scissors Versus Paper')
      print('You win!')
    elif playerInput == 's' and botInput == 'r':
      loss += 1
      print('Scissors Versus Rock')
      print('You lose!')
    elif playerInput == botInput:
      tie += 1
      print('You both chose the same! It is a tie')
    

  
    