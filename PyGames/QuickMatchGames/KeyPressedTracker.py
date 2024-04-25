import pygame

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()

# Set window size
width = 600
height = 400
screen = pygame.display.set_mode((width, height))

# Set window title
pygame.display.set_caption("f and j Key Tracker")

# Track key presses
pressed_keys = {"f": False, "j": False}


# Main program loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                pressed_keys["f"] = True
            elif event.key == pygame.K_j:
                pressed_keys["j"] = True
        
        # Check for key releases
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_f:
                pressed_keys["f"] = False
            elif event.key == pygame.K_j:
                pressed_keys["j"] = False

    # Fill the window with white
    screen.fill(WHITE)

    # Display text based on pressed keys
    font = pygame.font.Font(None, 32)
    if pressed_keys["f"]:
        text = font.render("f is pressed", True, BLACK)
    else:
        text = font.render("f is not pressed", True, BLACK)
    screen.blit(text, (100, 100))

    if pressed_keys["j"]:
        text = font.render("j is pressed", True, BLACK)
    else:
        text = font.render("j is not pressed", True, BLACK)
    screen.blit(text, (100, 150))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()