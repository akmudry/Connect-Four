import pygame

pygame.display.set_caption("Connect Four!")

WIN = pygame.display.set_mode((900, 600))
BOARD = pygame.Rect(100, 0, 700, 600)
board = pygame.Surface((700, 600))
column1 = pygame.Rect(100, 0, 100, 600)
column2 = pygame.Rect(200, 0, 100, 600)
column3 = pygame.Rect(300, 0, 100, 600)
column4 = pygame.Rect(400, 0, 100, 600)
column5 = pygame.Rect(500, 0, 100, 600)
column6 = pygame.Rect(600, 0, 100, 600)
column7 = pygame.Rect(700, 0, 100, 600)

def drawBoard(): #Drawing the board and all the circles
    WIN.fill((0, 0, 0))
    WIN.blit(board, BOARD)
    pygame.draw.rect(WIN, (0, 100, 200), BOARD)
    pygame.draw.circle(WIN, (255, 255, 255), (150, 50), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (150, 150), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (150, 250), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (150, 350), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (150, 450), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (150, 550), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (250, 50), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (250, 150), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (250, 250), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (250, 350), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (250, 450), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (250, 550), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (350, 50), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (350, 150), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (350, 250), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (350, 350), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (350, 450), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (350, 550), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (450, 50), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (450, 150), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (450, 250), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (450, 350), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (450, 450), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (450, 550), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (550, 50), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (550, 150), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (550, 250), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (550, 350), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (550, 450), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (550, 550), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (650, 50), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (650, 150), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (650, 250), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (650, 350), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (650, 450), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (650, 550), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (750, 50), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (750, 150), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (750, 250), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (750, 350), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (750, 450), 40)
    pygame.draw.circle(WIN, (255, 255, 255), (750, 550), 40)



def Connect4():
    run = True
    drawBoard()
    currentBoard = {1:"", 2:"", 3:"", 4:"", 5:"", 6:"", 7:""}
    player = 1
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePosition = pygame.mouse.get_pos()
                if column1.collidepoint(mousePosition):
                    if player == 1 and len(currentBoard[1]) < 6:
                        pygame.draw.circle(WIN, (255, 0, 0), (150, (550 - 100*len(currentBoard[1]))), 40)
                        currentBoard[1] += "R"
                        player = 2
                    elif len(currentBoard[1]) < 6:
                        pygame.draw.circle(WIN, (255, 255, 0), (150, (550 - 100*len(currentBoard[1]))), 40)
                        currentBoard[1] += "Y"
                        player = 1
                        
                if column2.collidepoint(mousePosition):
                    if player == 1 and len(currentBoard[2]) < 6:
                        pygame.draw.circle(WIN, (255, 0, 0), (250, (550 - 100*len(currentBoard[2]))), 40)
                        currentBoard[2] += "R"
                        player = 2
                    elif len(currentBoard[2]) < 6:
                        pygame.draw.circle(WIN, (255, 255, 0), (250, (550 - 100*len(currentBoard[2]))), 40)
                        currentBoard[2] += "Y"
                        player = 1
                        
                if column3.collidepoint(mousePosition):
                    if player == 1 and len(currentBoard[3]) < 6:
                        pygame.draw.circle(WIN, (255, 0, 0), (350, (550 - 100*len(currentBoard[3]))), 40)
                        currentBoard[3] += "R"
                        player = 2
                    elif len(currentBoard[3]) < 6:
                        pygame.draw.circle(WIN, (255, 255, 0), (350, (550 - 100*len(currentBoard[3]))), 40)
                        currentBoard[3] += "Y"
                        player = 1

                if column4.collidepoint(mousePosition):
                    if player == 1 and len(currentBoard[4]) < 6:
                        pygame.draw.circle(WIN, (255, 0, 0), (450, (550 - 100*len(currentBoard[4]))), 40)
                        currentBoard[4] += "R"
                        player = 2
                    elif len(currentBoard[4]) < 6:
                        pygame.draw.circle(WIN, (255, 255, 0), (450, (550 - 100*len(currentBoard[4]))), 40)
                        currentBoard[4] += "Y"
                        player = 1

                if column5.collidepoint(mousePosition):
                    if player == 1 and len(currentBoard[5]) < 6:
                        pygame.draw.circle(WIN, (255, 0, 0), (550, (550 - 100*len(currentBoard[5]))), 40)
                        currentBoard[5] += "R"
                        player = 2
                    elif len(currentBoard[5]) < 6:
                        pygame.draw.circle(WIN, (255, 255, 0), (550, (550 - 100*len(currentBoard[5]))), 40)
                        currentBoard[5] += "Y"
                        player = 1

                if column6.collidepoint(mousePosition):
                    if player == 1 and len(currentBoard[6]) < 6:
                        pygame.draw.circle(WIN, (255, 0, 0), (650, (550 - 100*len(currentBoard[6]))), 40)
                        currentBoard[6] += "R"
                        player = 2
                    elif len(currentBoard[6]) < 6:
                        pygame.draw.circle(WIN, (255, 255, 0), (650, (550 - 100*len(currentBoard[6]))), 40)
                        currentBoard[6] += "Y"
                        player = 1

                if column7.collidepoint(mousePosition):
                    if player == 1 and len(currentBoard[7]) < 6:
                        pygame.draw.circle(WIN, (255, 0, 0), (750, (550 - 100*len(currentBoard[7]))), 40)
                        currentBoard[7] += "R"
                        player = 2
                    elif len(currentBoard[7]) < 6:
                        pygame.draw.circle(WIN, (255, 255, 0), (750, (550 - 100*len(currentBoard[7]))), 40)
                        currentBoard[7] += "Y"
                        player = 1


                
        pygame.display.update()




    pygame.quit()

Connect4()
