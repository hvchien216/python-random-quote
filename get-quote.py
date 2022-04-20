import random

last = 13
rnd = random.randint(0, last)

print(rnd)

def primary():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[len(quotes)-1])
  print(rnd)

if __name__== "__main__":
  primary()
