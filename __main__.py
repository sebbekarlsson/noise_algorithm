from PIL import Image
import random
from math import *


# This function puts data on each pixel, (we need something to start with)
def precompile(image, pixels, amount):
    for x in range(0, image.width):
            for y in range(0, image.height):
                r = int(255 / random.randint(1, amount))
                g = int(255 / random.randint(1, amount))
                b = int(255 / random.randint(1, amount))
                pixels[x, y] = (r, g, b)

    return pixels

# Run the program
def main():

    # How many times should we compile?
    compiles = 100

    # Width and height of image
    width = 640
    height = 480

    # Let's create the image
    image = Image.new('RGB', (width, height))
    pixels = image.load()
    
    # Let's pre-compile the image. (putting data on each pixel so that we have something to start with)
    pixels = precompile(image, pixels, 6)

    # Compile
    for i in range(0, compiles):

        print('{p}%\r'.format(p=(i / compiles) * 100 ), end='\r')

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
                medium_r =\
                (
                    int((left_pixel[0])) +
                    int((right_pixel[0])) +
                    int((top_pixel[0])) +
                    int((bottom_pixel[0]))
                ) / 4

                medium_g =\
                (
                    int((left_pixel[1])) +
                    int((right_pixel[1])) +
                    int((top_pixel[1])) +
                    int((bottom_pixel[1]))
                ) / 4

                medium_b =\
                (
                    int((left_pixel[2])) +
                    int((right_pixel[2])) +
                    int((top_pixel[2])) +
                    int((bottom_pixel[2]))
                ) / 4

                # Setting the values of the current pixel
                current_pixel = (int(medium_r), int(medium_g) , int(medium_b))
                
                # Saving changes to current pixel
                pixels[x, y] = current_pixel

        # Save image
        image.save("results/result-{v}.png".format(v=i))


if __name__ == '__main__':
    main()