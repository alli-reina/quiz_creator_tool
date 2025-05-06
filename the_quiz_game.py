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

# Load the intro assets
intro_background_image = pygame.image.load("intro_background.png")
intro_background_image = pygame.transform.scale(intro_background_image, (window_width, window_height))

start_button_image = pygame.image.load("start_button.png")
start_button_image = pygame.transform.scale(start_button_image, (200, 80))
start_button_rectangle = start_button_image.get_rect(topleft=(445,340))