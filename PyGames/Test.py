import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Multiline Text Input")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define font
font = pygame.font.Font(None, 32)

# Function to draw text on the screen
def draw_text(surface, text, pos, color):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # Width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, True, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

# Main loop
def main():
    text = ""
    text_pos = (50, 50)
    text_color = BLACK

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    text += "\n"  # Add a newline character when Enter key is pressed
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]  # Remove the last character when Backspace key is pressed
                else:
                    text += event.unicode  # Add the typed character to the text

        # Clear the screen
        window.fill(WHITE)

        # Draw the text on the screen
        draw_text(window, text, text_pos, text_color)

        # Update the display
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
