# QUIZ GAME made by: JONALYN ANTOC

# Initialize Pygame and required libraries
import pygame
import sys
import random

pygame.init()

# Load the font
minecraft_font = pygame.font.Font("minecraft.ttf", 26)

# Set up the game window
window_width, window_height = 1080, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("QUIZ GAME")
clock = pygame.time.Clock()

# Load intro screen assets
intro_background_image = pygame.image.load("intro_background.png")
intro_background_image = pygame.transform.scale(intro_background_image, (window_width, window_height))

start_button_image = pygame.image.load("start_button.png")
start_button_image = pygame.transform.scale(start_button_image, (200, 80))
start_button_rectangle = start_button_image.get_rect(topleft=(445, 340))

# Define the function load_quiz_data(file_path)
def load_quiz_data(file_path):
    with open(file_path, "r", encoding="utf-8") as quiz_file:
        lines = quiz_file.readlines()
    
    quiz_list = []
    current_quiz = {}

    for line in lines:
        line = line.strip()
        if line.startswith("Question:"):
            current_quiz["question"] = line.replace("Question:", "").strip()
        elif line.startswith(("A)", "B)", "C)", "D)")):
            prefix, choice_text = line.split(")", 1)
            choice_key = prefix.strip().lower()
            current_quiz[choice_key] = choice_text.strip()
        elif line.startswith("Answer:"):
            current_quiz["answer"] = line.replace("Answer:", "").strip().lower()
        elif line == "---":
            quiz_list.append(current_quiz)
            current_quiz = {}
    
    return quiz_list

# Define the function wrap_text_to_fit(text, font, max_width)
def wrap_text_to_fit(text, font, max_width):
    words = text.split(" ")
    lines = []
    current_line = ""
    for word in words:
        test_line = f"{current_line} {word}".strip()
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)
    return lines

# Define the function start_quiz()
def start_quiz():
    quiz_background_image = pygame.image.load("quiz_template.png")
    quiz_background_image = pygame.transform.scale(quiz_background_image, (window_width, window_height))

    feedback_background_image = pygame.image.load("feedback_template.png")
    feedback_background_image = pygame.transform.scale(feedback_background_image, (window_width, window_height))

    score_background_image = pygame.image.load("score_template.png")
    score_background_image = pygame.transform.scale(score_background_image, (window_width, window_height))

    quiz_data_list = load_quiz_data("quiz.txt")
    random.shuffle(quiz_data_list)

    current_question_index = 0
    player_score = 0
    show_feedback_screen = False
    feedback_message = ""
    feedback_start_time = 0
    choice_hitboxes = {}

    # Quiz loop
    is_quiz_running = True
    while is_quiz_running:
        clock.tick(60)
        window.blit(quiz_background_image, (0, 0))

        if current_question_index >= len(quiz_data_list):
            window.blit(score_background_image, (0, 0))
            score_text = minecraft_font.render(f"You got {player_score} out of {len(quiz_data_list)} correct!", True, (0, 0, 0))
            score_x_position = window_width // 2 - score_text.get_width() // 2
            score_y_position = 510
            window.blit(score_text, (score_x_position, score_y_position))
        else: 
            current_question = quiz_data_list[current_question_index]
            choice_hitboxes.clear()

            wrapped.question_lines = wrap_text_to_fit(current_question["question"], minecraft_font, 600)
            for line_index, line_text in enumerate(wrapped_question_lines):
                line_surface = minecraft_font.render(line_text, True, (0, 0, 0))
                window.blit(line_surface, (200, 190 + line_index * 30))

                choice_positions = {
                    "a": (179, 390),
                    "b": (593, 390),
                    "c": (179, 490),
                    "d": (599, 490),
                }
                
                for choice_key in ["a", "b", "c", "d"]:
                    choice_display_text = f"{choice_key.upper()}) {current_question[current_question[choice_key]]}"
                    choice_surface = minecraft_font.render(choice_display_text, True, (0, 0, 0))
                    choice_rectangle = choice_surface.get_rect(topleft=choice_positions[choice_key])
                    window.blit(choice_surface, choice_rectangle)
                    choice_hitboxes[choice_key] = choice_rectangle

                if show_feedback_screen:
                    window.blit(feedback_background_image, (0, 0))
                    if "Coreect" in feedback_message:
                        feedback_surface = minecraft_font.render("CORRECT!", True, (0, 150, 0))
                        else: 
                            correct_answer_letter = current_question["answer"].upper()
                            feedback_message = f"WRONG! CORRECT ANSWER IS: {correct_answer_letter}"
                            feedback_surface = minecraft_font.render(feedback_message, True, (200, 0, 0))

                        feedback_x_position = window_width // 2 - feedback_surface.get_width() // 2
                        window/blit(feedback_surface, (feedback_x_position, 230))

                        if pygame.time.get.ticks() - feedback_start_time > 2000:
                            current_question_index += 1
                            show_feedback_screen = False
                
                pygame.display.flip()

                # Event handling loop
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        is_quiz_running = False
                        pygame.quit()
                        sys.exit()

                    if (event.type == pygame.MOUSEBUTTONDOWN
                    and not show_feedback_screen
                    and current_question_index < len(quiz_data_list)):
                    mouse_position = pygame.mouse.get_pos()
                    for choice_letter, hitbox in choice_hitboxes.items():
                        if hitbox.collidepoint(mouse_position):
                            correct_choice = quiz_data_list[current_question_index]["answer"]
                            if choice_letter == correct_choice:
                                feedback_message = "Correct!"
                                player_score += 1
                            else:
                                feedback_message = f"WRONG! CORRECT ANSWER IS: {correct_choice.upper()}"
                            feedback_start_time = pygame.time.get_ticks()
                            show_feedback_screen = True

# Intro screen loop
intro_running = True
while intro_running:
    clock.tick(60)
    window.blit(intro_background_image, (0,0))
    window.blit(start_button_image, start_button_rectangle.topleft)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            intro_running = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            if start_button_rectangle.collidepoint(mouse_position):
                intro_running = False
                start_quiz()

# End the game
pygame.quit()
