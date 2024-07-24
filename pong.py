#
#
# A simple pong game made my following the tutorial on the pygame website
#
#

try:
    # Import all necessary modules
    import sys
    import random
    import math
    import os
    import getopt
    import pygame
    from socket import *
    from pygame.locals import *

    # Handle error in loading modules
except ImportError as err:
    print(f"couldn't load module. {err}")
    sys.exit(2)

# Function to load png
def load_png(name):
    """ Load image and return image object"""
    fullname = os.path.join("data", name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except FileNotFoundError:
        print(f"Cannot load image: {fullname}")
        raise SystemExit
    return image, image.get_rect()
