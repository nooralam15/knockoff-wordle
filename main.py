#Wordle Knockoff Code

#Import libraries
import pygame, sys
pygame.init()
 
#Set up the drawing window
screen = pygame.display.set_mode([800, 900])

#Set up fonts and colours
font = pygame.font.SysFont(None, 40)
color = (255, 0, 0)


#user_text = ''
#text = 'hello'
#var = list(text)

#Create a functon that controls user text input 
def userTextControl(user_text):
  text_box = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(350, 700, 90, 40), 2)
  text_render = font.render(user_text, True, (255, 0, 0))
  screen.blit(text_render, text_box)
  

#Create a gameboard class
class Board:
  #Initialize constructor
  def __init__(self, location):
    self.board = [["", "", "", "", ""],
                  ["", "", "", "", ""],
                  ["", "", "", "", ""],
                  ["", "", "", "", ""], 
                  ["", "", "", "", ""],
                  ["", "", "", "", ""]]               
    self.location = location
    
  #Create a board display method
  def boardDisplay(self):
    y = 0
    for row in self.board:
        x = 220
        y += 100
        for col in row:
            pygame.draw.rect(self.location, color, pygame.Rect(x, y, 40, 40), 2)
            x += 80
   
#Create a main function that runs the program
def main():
  #Create a loop that will run the program 
  loop = True
  while loop:
    global user_text
    user_text = ''
    

        #Keyboard events 
    for event in pygame.event.get(): #Checks to see if window close is cllcked
        if event.type == pygame.QUIT:
            loop = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_BACKSPACE: 
            user_text = user_text[0:-1]
          else:
            user_text += event.unicode
            print(user_text)

    #set up the screen
    screen.fill((255, 255, 255))

    #Csll the board character 
    board = Board(screen)
    board.boardDisplay()

    #Display user input
    text_box = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(350, 700, 90, 40), 2)
    text_render = font.render(user_text, True, (255, 0, 0))
    screen.blit(text_render, text_box)

    

    #display the screen
    pygame.display.update()


main()










