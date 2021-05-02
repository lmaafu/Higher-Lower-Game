# function go here 
def instructions ():
  print("**** Welcome to the Higher or Lower Game ****")
  print("For each game you will be asked to....")
  print("- Enter a 'low' and 'high' number. The compute'r will randomly generate a 'secret' number between your two chosen numbers. It will use these numbers for all the rounds in agiven game.")
  print(" - The computer will calculate how many guesses yo are allowed ")
  print("- enter the onumber of rounds you want to play")
  print("- guess the secret number")
  print()
  print()
  print("Good Luck!")
  
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
