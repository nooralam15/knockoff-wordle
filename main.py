#Wordle Knockoff Code
import pygame, sys
pygame.init()
 
 # Set up the drawing window
screen = pygame.display.set_mode([800, 1000])
color = (255, 0, 0)
font = pygame.font.SysFont(None, 20)
user_text = ''
# Run until the user asks to quit
running = True
while running:

    screen.fill((255, 255, 255))
    board = [["", "", "", "", ""],
             ["", "", "", "", ""],
             ["", "", "", "", ""],
             ["", "", "", "", ""], 
             ["", "", "", "", ""],
             ["", "", "", "", ""]]
    y = 0
    for row in board:
        x = 220
        y += 100
        for col in row:
            pygame.draw.rect(screen, color, pygame.Rect(x, y, 40, 40), 2)
            x += 80
    
    text_render = font.render(user_text, True, (255, 0, 0))
    screen.blit(text_render, (200, 200))

        # Flip the display
    pygame.display.flip()

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            user_text += event.unicode

# Done! Time to quit.
pygame.quit()