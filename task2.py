file ="E:\data lakehouse.png"
pic= makePicture(file)
pixels = getPixels(pic)
setRed(pixels[0],getRed(pixels[0])*10)
pic.explore()  
