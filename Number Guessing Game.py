def main():

  import random

  print("Welcome to Super Number Guesser 64!\n\n" + "Choose a maximum range number\n" + "The computer will create a random number from one to 'the number you choose'\n" + "Guess numbers until you guess the number the computer has chosen.")
  top_of_range = input("Type a number: ")

  if top_of_range.isdigit():
      top_of_range = int(top_of_range)

      if top_of_range <= 0:
          print("Pleaes type a number larger than 0.")
          quit()
              
  else:
      print("Please type a number next time.")
      quit()
      
  random_number = random.randint(1, top_of_range)
  guesses = 0

  while True:
      guesses += 1
      user_guess = input("Make a guess: ")
      if user_guess.isdigit():
          user_guess = int(user_guess)
          
      else:
          print("Please type a number next time.")
          continue

      if user_guess == random_number:
          print("You got it!")
          break

      elif user_guess > random_number:
          print("You got it wrong!  You are above the number.")
      else:
          print("You got it wrong!  You are below the number.")

  print("You got it in " + str(guesses) + " guesses.")
  game_restart()

def game_restart():
  restart = input("Do you want to play again?").lower()
  if restart == "yes":
    print("You can do it!")
    main()
  elif restart == "no":
    print("You can do it?!")
    quit()
  else:
    print("Please say 'yes' or 'no'.")
    game_restart()

main()
