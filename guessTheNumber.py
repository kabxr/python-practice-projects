import random

secretNum = random.randint(1,20)
print("Guess a number between 1 and 20")
print("You have 6 tries :)")

for guessesTaken in range(0,6):
  print('Take a guess')
  guess = int(input())
  if guess < secretNum:
    print('guess is too low')
  elif guess > secretNum:
    print('guess is too high')
  else:
    break

if guess == secretNum:
  print(f"Great! You got the number in {guessesTaken + 1} tries")
else:
  print(f"You failed, the correct number was {secretNum}")