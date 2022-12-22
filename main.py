
# required imports
import pygame,sys,random
from pygame.locals import *
from button import Button
from tabulate import tabulate

pygame.init()

def tictactoe():
  #Open Pygame window
  screen = pygame.display.set_mode((640, 480)) # add RESIZABLE or FULLSCREEN
  
  # set title as Tic Tac Toe
  pygame.display.set_caption("tic tac toe")
  color = pygame.color.THECOLORS["black"] # background colour

  # sets up the table of the game
  tab = pygame.image.load("resources/ttt.png").convert() #the grid
  tab.set_colorkey((0,0,0))
  tab_pos = (170,90)

  # aspects of the game (yellow emoji)
  yellow = pygame.image.load("resources/yellow.png").convert()
  yellow.set_colorkey((0,0,0))
  yellow_list = []

  # aspects of the game (purple emoji)
  purple = pygame.image.load("resources/purple.png").convert()
  purple.set_colorkey((0,0,0))
  purple_list=[]
  inspect_line=[]
  cont=0
  selected=0

  #stores the number of scores and levels
  cpu_level=2
  win = 0
  player=0
  cpu=0
  lose=0
  draw=0
  draw2=0
  r=0
  time=0
  turn="player"
  
  # text font in the game
  font=pygame.font.SysFont('dejavuserif', 20)       

  #location of the tabs for the emojies
  tab_case=[(170,90),(270,90),(370,90),
           (170,190),(270,190),(370,190),
           (170,290),(270,290),(370,290)]
  
  #sets 't' as the tab case
  t = tab_case
  win_line = [ [t[0],t[1],t[2]], [t[3],t[4],t[5]],[t[6],t[7],t[8]],
             [t[0],t[3],t[6]], [t[1],t[4],t[7]], [t[2],t[5],t[8]],
             [t[0],t[4],t[8]], [t[6],t[4],t[2]] ] # all the possible winning tabs; 3 in a row
  pygame.key.set_repeat(400, 30)

  # writing the module
  while True:
    #loop speed limitation
    pygame.time.Clock().tick(3) #30 frames per second is enough
   
    for event in pygame.event.get():
      if event.type == pygame.QUIT:    #wait for events
        pygame.quit()
        sys.exit() 
              
      #mouse commands
      if event.type == MOUSEBUTTONDOWN:
         if win or lose or draw:
            yellow_list = []; purple_list =[]; win=0; lose=0; draw=0; screen.fill(color);turn = "player"
            screen.blit(tab,tab_pos);pygame.display.flip()
         if event.button == 1:
            if turn == "player":
               for case in tab_case:
                 if event.pos[0]>case[0]and event.pos[0]<case[0]+100 \
                 and event.pos[1]>case[1]and event.pos[1]<case[1]+100 :
                     if not case in yellow_list and not case in purple_list:
                        selected = 1
                        yellow_list.append(case)
                        screen.blit(yellow, case) #displays the yellow emoji
                        
               for line in win_line:
                   cont = 0
                   for case in line:
                       for yellow1 in yellow_list:
                           if yellow1 == case:cont += 1
                   if cont == 3 and not lose:
                      win = 1
               if win:
                  player += 1
               if selected:
                  cont = 0
                  selected = 0
                  turn="cpu"
               
    if turn == "cpu" and not win:
      time+=1
      if time==3:
       time=0
       if not selected and cpu_level>=1:
         
             for line in win_line:
              if not selected:
                 cont=0
                 for case in line:
                    for purple1 in purple_list:
                     if purple1==case:cont+=1
                     
              if cont == 2 and not selected:
                 for case in line:
                     for purple1 in  purple_list:
                         if case_inspect != purple1:
                            if not case in purple_list and not case in yellow_list:
                             selected=1
                             purple_list.append(case)
                             screen.blit(purple, case) #displays the purple emoji
        
       if not selected and cpu_level==2:
         
             for line in win_line:
              if not selected:
                 cont = 0
                 for case in line:
                    for yellow1 in yellow_list:
                     if yellow1 == case:cont += 1
                       
              if cont==2 and not selected:
                 for case in line:
                     for yellow1 in yellow_list:
                         if case != yellow1:
                            if not case in purple_list and not case in yellow_list:
                             selected = 1
                             purple_list.append(case)
                             screen.blit(purple, case)
  
                             
       if not selected and cpu_level>=1:
         
             for line in win_line:
              if not selected:
                 cont = 0
                 for case in line:
                    for purple1 in purple_list:
                     if purple1 == case:cont += 1
                    for yellow1 in yellow_list:
                     if yellow1 == case:cont = 0
            
              if cont == 1 and not selected:
                for index in range(len(line)):
                    for purple1 in  purple_list:
                      if not selected:
                        if line[index] == purple1 and line[index] != line[len(line)-1]:
                          if not line[index+1] in yellow_list and not line[index+1] in yellow_list:
                            selected = 1
                            purple_list.append(line[index+1])
                            screen.blit(purple,line[index+1])
                        elif line[index] == purple1 and line[index] == line[len(line)-1]:
                          if not line[index-1] in purple_list and not line[index-1] in yellow_list:
                            selected = 1
                            purple_list.append(line[index-1])
                            screen.blit(purple,line[index-1])
  
                            
       if not selected and cpu_level>=0:
         
         for case in tab_case:
           if not selected:
             cont = 0
             r=random.randint(0,8)
             for yellow1 in yellow_list:
                 if tab_case[r] == yellow1:cont += 1
             for purple1 in purple_list:
                 if tab_case == case:cont += 1
             if not cont:
                if not tab_case[r] in purple_list and not tab_case[r] in yellow_list:
                   selected = 1
                   purple_list.append(tab_case[r])
                   screen.blit(purple,tab_case[r])
            
       if not selected and cpu_level>=0:
         
         for case in tab_case:
           if not selected:
             cont = 0
             for yellow1 in yellow_list:
                 if yellow1 == case:cont += 1
             for purple1 in purple_list:
                 if purple1 == case:cont += 1
             if not cont:
                if not case in purple_list and not case in yellow_list:
                   selected = 1
                   purple_list.append(case)
                   screen.blit(purple,case)
                   
       for purple1 in purple_list:
           for line in win_line:
               cont=0
               for case in line:
                   if purple1==case:
                      inspect_line=line
                      for case_inspect in inspect_line:
                           for purple2 in  purple_list:
                               if case_inspect == purple2:
                                  cont += 1         
               if cont == 3:
                  lose=1
       if lose:
          cpu += 1
       cont = 0
       cont2 = 0
       selected = 0
       turn = "player"
       
    if not win and not lose and not draw:
      for case in tab_case:
          for yellow1 in yellow_list:
              if yellow1 == case:cont += 1
          for purple1 in purple_list:
              if purple1 == case:cont += 1
          if cont == 9:
             draw = 1
             draw2 += 1
      cont = 0
      
    screen.fill(color)
    
    if win:
       text=font.render(("YOU WIN!"), True, (0,250,0));screen.blit(text,(270,400))
    elif lose:
       text=font.render(("YOU LOSE!"), True, (250,0,0));screen.blit(text,(270,400))
    elif draw:
       text=font.render(("IT'S A TIE!"), True, (0,0,250));screen.blit(text,(285,400))
       
    text=font.render(("cpu level = "+str(cpu_level)), True, (250,250,250));screen.blit(text,(480,0))
    text=font.render(("cpu = "+str(cpu)), True, (250,0,0));screen.blit(text,(180,0))
    text=font.render(("You = "+str(player)), True, (0,250,0));screen.blit(text,(0,0))
    text=font.render(("Draw = "+str(draw2)), True, (0,0,250));screen.blit(text,(340,0))
  
    screen.blit(tab,tab_pos)
    for yellow_pos in yellow_list:
        screen.blit(yellow, yellow_pos)
    for purple_pos in purple_list:
        screen.blit(purple, purple_pos)
  
    pygame.display.flip()

#menu screen 
pygame.init()
SCREEN = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Menu")
font = "font.ttf"

BG = pygame.image.load("bg.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)

# blits image to screen when user inputs something, e.g quit input = thank you message.
def push_image(title,fileName):
  #grab elements from the pygame interface
  infoObject = pygame.display.Info()

#create the display surface to grab the size of the pygame screen
  display_surface = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
  #create the window with the title given
  pygame.display.set_caption(title) 

  #convert the file to a png for pygame to use
  image = pygame.image.load(fileName).convert()

  #scale the image to the pygame window size
  image = pygame.transform.scale(image, (infoObject.current_w, infoObject.current_h))

  #push the image out to the pygame screen
  display_surface.blit(image, (0, 0)) 

  #refresh the screen with the new image
  pygame.display.update()

#function to show thank you image when the user clicks quit on the menu
def ty_image():
  push_image("ty","ty.png")
  pygame.display.update()

#function to show instructions when the user clicks instructions on the menu
def instruction():
  push_image("instruction","instruction.png")
  pygame.display.update()

#function to create the menu
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0)) # blits a black screen 

        MENU_MOUSE_POS = pygame.mouse.get_pos() #Returns the x and y position of the mouse cursor. The position is relative to the top-left corner of the display but is always constrained to the screen.

        menutext = get_font(28).render("TIC TAC TOE", True, "#C5E384")
        MENU_RECT = menutext.get_rect(center=(200, 25))

        playbutton = Button(image=pygame.image.load("Rect.png"), pos=(200, 115), text_input="PLAY", font=get_font(23), base_color="#d7fcd4", hovering_color="Green") # creating buttons

        insbutton = Button(image=pygame.image.load("Rect.png"), pos=(200, 215), text_input="INSTRUCTIONS", font=get_font(23), base_color="#d7fcd4", hovering_color="Cyan")
        
        quitbutton = Button(image=pygame.image.load("Rect.png"), pos=(200, 315), text_input="QUIT", font=get_font(23), base_color="#d7fcd4", hovering_color="Red")

        SCREEN.blit(menutext, MENU_RECT)

        for button in [playbutton, insbutton, quitbutton]:
            button.changeColor(MENU_MOUSE_POS) # if mouse hovers over options changes colors 
            button.update(SCREEN)
        
        for event in pygame.event.get(): # quits the game 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: #clicks play/begins game 
                if playbutton.checkForInput(MENU_MOUSE_POS):
                    tictactoe() # calls and plays game
                if insbutton.checkForInput(MENU_MOUSE_POS):
                    instruction() # displays the image with instructions
                    pygame.time.wait(25000) # displays the image in the given time

                if quitbutton.checkForInput(MENU_MOUSE_POS):
                    ty_image() # show thank you image
                    pygame.time.wait(5000) # displays the image in the given time
                    pygame.quit() # exit
                    sys.exit()

        pygame.display.update() # continiously updates screen or resets screen when arguement is made

main_menu()