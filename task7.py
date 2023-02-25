def decreaseVolume(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value * 5)

file = pickAFile()
s = makeSound(file)
explore(s)
decreaseVolume(s)
explore(s)

