from PIL import Image
import random
from math import *


# This function puts data on each pixel, (we need something to start with)
def precompile(image, data):
    pixels = image.load()

    for x in range(0, image.width):
            for y in range(0, image.height):
                value = int(data)
                pixels[x, y] = (value, value, value)

    return pixels

# Run the program
def main():

    # How many times should we compile?
    compiles = 5

    # Width and height of image
    width = 640
    height = 480

    # Let's create the image
    image = Image.new('RGB', (width, height))
    
    # Let's pre-compile the image. (putting data on each pixel so that we have something to start with)
    pixels = precompile(image, compiles) 

    # Compile
    for i in range(0, compiles):

        # Loop through each pixel
        for x in range(0, width):
            for y in range(0, height):

                # Collect surrounding pixels
                left_pixel = pixels[max(0, x - 1), max(0, y - 1)]
                right_pixel = pixels[min(width - 1, x + 1), min(height - 1, y + 1)]
                top_pixel = pixels[x, max(0, y - 1)]
                bottom_pixel = pixels[x, min(height - 1, y + 1)]
                current_pixel = pixels[x, y]

                # Lets calculate the medium_value of each pixel
                medium_value = ((left_pixel[0] + right_pixel[0] + top_pixel[0] + bottom_pixel[0]) / 4)
                
                # Calculating our final value and adding a random value to it
                value = int(medium_value + random.randint(0, 24))

                # Setting the values of the current pixel
                current_pixel = (value, value , value)
                
                # Saving changes to current pixel
                pixels[x, y] = current_pixel

    # Saving image
    image.save("result.png")


if __name__ == '__main__':
    main()