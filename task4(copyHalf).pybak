def copyHalf(picture):
    pixels = getPixels(picture)
    for index in range(0,len(pixels)/2):
        pixel1 = pixels[index]
        color1 = getColor(pixel1)
        pixel2 = pixels[index + len(pixels)/2]
        setColor(pixel2,color1)

         
file = pickAFile()
pic = makePicture(file)
copyHalf(pic)
explore(pic)
