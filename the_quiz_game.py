import pygame
import sys

pygame.init ()

# Load the font wanted
minecraft_font = pygame.font.Font("Minecraft.ttf", 26)

# Window Settings
window_width, window_height = 1080, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("QUIZ GAME")
clock = pygame.time.Clock()

