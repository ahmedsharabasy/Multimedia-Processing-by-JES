#Reduce the amount of red in a picture by 50%.
def decreaseRed(picture):
  for px in getPixels(picture):
    value = getBlue(px)
    setBlue(px, value * 0.5)
    
file = pickAFile()
pic = makePicture(file)
decreaseRed(pic)
pic.explore()
