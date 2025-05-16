#given two numbers: width of an image,height of an image
#You need to check: If the width is more than the height, the image is Landscape (wide).Otherwise, the image is Portrait (tall).
#function named "isLandscape"
#width and height as arguments

def isLandscape(width,height):
    if width>height:
        return "Landscape"
    else:
        return "Portrait"
width = int(input("Enter image width: "))
height = int(input("Enter image height: "))
result=isLandscape(width,height)
print("The image is in:",result,"orientation.")

