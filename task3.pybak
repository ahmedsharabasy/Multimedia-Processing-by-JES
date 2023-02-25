def darken(picture):
    for px in getPixels(picture):
        color = getColor(px)
        color = makeDarker(makeDarker(makeDarker(color)))
        setColor(px,color)



file = pickAFile()
pic = makePicture(file)
darken(pic)
show(pic)