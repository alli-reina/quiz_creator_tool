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

def load_quiz_data(file_path):
    with open(file_path, "r", encoding="utf-8") as quiz_file:
        lines = quiz_file.readlines()

    quiz_list = []
    current_quiz = {}

    for line in lines:
        line = line.strip()
        if line.startswith("Question:"):
            current_quiz["question"] = line.replace("Question:", "").strip()
        elif line.startswith("A)") or line.startswith("B)") or line.startswith("C)") or line.startswith("D)"):
            prefix, choice_text = line.split(")", 1)
            choice_key = prefix.strip().lower()
            current_quiz[choice_key] = choice_text.strip()
        elif line.startswith("Answer:"):
            current_quiz["answer"] = line.replace("Answer:", "").strip().lower()
        elif line == "---":
            quiz_list.append(current_quiz)
            current_quiz = {}

    return quiz_list
