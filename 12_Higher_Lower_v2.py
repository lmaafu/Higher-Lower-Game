import math
import random

# HL  component 1 - Get (and check) user input 
# Function goes here 
# displays instructins for the user 
def instructions ():
  statement_generator(" Welcome to the Higher or Lower Game ", "*")
  print("For each game you will be asked to....")
  print("- Enter a 'low' and 'high' number. The compute'r will randomly generate a 'secret' number between your two chosen numbers. It will use these numbers for all the rounds in agiven game.")
  print(" - The computer will calculate how many guesses yo are allowed ")
  print("- enter the onumber of rounds you want to play")
  print("- guess the secret number")
  print()
  print()
  print("Good Luck!")

# Checks if the use asnwers yes or no for othe given queston 
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes/no")

# Decorations for the sides of the heading 
def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

# integer Checker 
def int_check(question, low=None, high=None, exit_code = None): 

  valid = False
  while not valid: 
    response = input(question).lower()

    if exit_code == "xxx" and response == "xxx":
      return response
    elif exit_code == "" and response == "":
      return response

    situation = ""

    if low is not None and high is not None: 
      situation = "both"
    elif low is not None and high is None:
      situation = "low only "

    try:
        response = int(response)

        # checks input is not too high or
        # too low if a both upper and lower bounds 
        # are specified 
        if situation == "both":
          if response < low or response > high:
            print("Please enter a number between {} and {}".format(low, high))
            continue

        # checks input is not too low 
        elif situation == "low only ":
          if response < low:
              print("Plese enter a number that is more than (or equal to) {}".format(low))
              continue

        return response 

    # Checks iput is integer 
    except ValueError:
      print("Please enter an integer")
      continue

  
# Main routine 
played_before= yes_no("Have you played the game before? ")
print()

if played_before == "no":
    instructions()
    print()

# Set up the gam parameters (range, number of numbers)
low = int_check("Low Number: ")
print()
high = int_check(" High Number: ", low + 1)
print()
rounds = int_check(" Rounds: ", 0, exit_code = "")

# works out nmber of guesses 
num_range = high - low + 1
max_raw = math.log2(num_range)  # finds maximum # of guesses using math.log2
max_upped = math.ceil(max_raw)  # rounds up (ceil----> ceiling )
max_guesses = max_upped + 1

print("Max Guesses: {}".format(max_guesses ))
print()
# Rounds

rounds_lost = 0
rounds_won = 0  
rounds_played = rounds_won + rounds_lost 
# Rounds Heading 


# Continous rounds heading 
if rounds == "":
  heading = " Continuous Mode : Round {}".format(rounds_played + 1)
  print(heading)
  # Specific number of rounds 
else:
  heading = "Round {} of {} ".format(rounds_played + 1, rounds)
  print(heading)


for item in range(0, rounds):

  secret = random.randint(low, high)
  print("Spoiler alert, the secret is", secret)
  guesses_allowed = max_guesses 

  already_guessed =[]
  guesses_left = guesses_allowed
  num_won = 0

  guess = ""

  while guess != secret and guesses_left >= 1:
    guess = int_check("Guess: ", low, high)  # replace this with function

    #v checks that guess is not a duplicate 
    if guess in already_guessed:
      print("You already guessed that number! Please try again ","You *still* have {} guesses left".format(guesses_left))
      continue

    guesses_left -= 1
    already_guessed.append(guess)

    # Compare number if we have guesses left and ask use to try again 
    if guesses_left >= 1:

      if guess < secret:
        print("Too low, try a higher number. Guesses left : {}".format(guesses_left))

      elif guess > secret:
        print("Too high, try a lower number. Guesses left : {}".format(guesses_left))

    # compare numbers if user is on their last guess
    else:
      if guess < secret:
        print("Too low!")
      elif guess > secret:
        print("Too high!")
  
  # If user is correct, output success message based on number of guesses needed. 
    if guess == secret:
      if guesses_left == guesses_allowed -1:
        print("Amazing! You got it")
      else:
        print("Well done! You got it")

      break
    
  # HL component 11 - Maximum Guesses Calculator

