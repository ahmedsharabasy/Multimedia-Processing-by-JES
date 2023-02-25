def normalize(sound):
  largest = 0
  for s in getSamples(sound):
    largest = max(largest,getSampleValue(s))
  multiplier = 32767.0/largest
  print("Largest sample value in original sound was",largest)
  print("Multiplier is",multiplier)
  for s in getSamples(sound):
    louder = multiplier * getSampleValue(s)
    setSampleValue(s,louder)  

file = pickAFile()
s = makeSound(file)
normalize(s)
explore(s)