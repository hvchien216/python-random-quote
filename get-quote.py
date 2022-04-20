def primary():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes)
  print(quotes[0])
  # Responsive is better than fast

if __name__== "__main__":
  primary()
