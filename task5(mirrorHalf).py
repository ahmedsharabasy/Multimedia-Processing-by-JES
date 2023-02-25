def copyHalf(picture):
    pixels = getPixels(picture)
    target = len(pixels)-1
    for index in range(0,len(pixels)/2):
        pixel1 = pixels[index]
        color1 = getColor(pixel1)
        pixel2 = pixels[target]
        setColor(pixel2,color1)
        target = target-1

         
file = pickAFile()
pic = makePicture(file)
copyHalf(pic)
explore(pic)