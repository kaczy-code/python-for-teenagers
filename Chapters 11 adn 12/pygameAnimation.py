# import our modules
import pygame
from pygame.locals import *
import sys
import random

# Initialize our pygame modules
pygame.init()

# Create tuples for our colors
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)

# Create our main game window - last time we named it screen
# Let's give it a different name this time
gameWindow = pygame.display.set_mode((800, 600))

# Set the caption/title for our animation
pygame.display.set_caption('Box Animator 5000')
