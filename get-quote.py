import random

def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt", "r+") # r+ read and write mode

  f.write('Same quote for edit programaticaly \n')
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  rnd = random.randint(0, last)

  print(quotes[rnd], sep="", end="") # remove a new line after print

if __name__== "__main__":
  primary()
