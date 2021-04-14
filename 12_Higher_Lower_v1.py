# HL  component 1 - Get (and check) user input 

# To do 
# Check a lowest is an integer (any integer)
# Check that highest is more than lowest (lower bound only)
# Check that rounds is more than 1 (upper bound only)
# Check that guss is betweeen lowest and highest 9
# lower and upper bound0


# Number checking function goes here 
def int_check(question, low=None, high=None): 

  situation = ""

  if low is not None and high is not None: 
    situation = "both"
  elif low is not None and high is None:
    situation = "low only "

  while True:

    try:
        response = int(input(question))

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

lowest = int_check("Low Number: ")
highest = int_check(" High Number: ", lowest + 1)
rounds = int_check( "Rounds: ", 1)
guess = int_check("Guess: ", lowest, highest)

# HL component 5 - no duplicates

# To Do 
# set up empty list called already_guessed
# when user guesses, add guess to list 
# for each guess, check that number is not in already_guessed

# HL component 5 - Prevents duplicate gusses

SECRET = 7
GUESSES_ALLOWED = guess

already_guessed =[]
guesses_left = GUESSES_ALLOWED
num_won = 0

guess = ""

while guess != SECRET and guesses_left >= 1:
  guess = int(input("Guesses: "))  # replace this with function

  #v checks that guess is not a duplicate 
  if guess in already_guessed :
    print("You already guessed that number! Please try again ","You *still* have {} guesses left".format(guesses_left, ))
    continue
  
  guesses_left -= 1
  already_guessed.append(guess)

  if guesses_left >= 1:

    if guess < SECRET:
      print("Too low, try a higher number. Guesses left : {}".format(guesses_left))

    elif guess > SECRET:
      print("Too high, try a lower number. Guesses left : {}".format(guesses_left))

  else:
    if guess < SECRET:
      print("Too low!")
    elif guess > SECRET:
      print("Too high!")

if guess == SECRET:
  if guesses_left == GUESSES_ALLOWED -1:
   print("Amazing! You got it")
else:
  print("Well done! You got it")
  
  # HL component 11 - Maximum Guesses Calculator

