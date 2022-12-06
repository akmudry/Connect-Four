import pygame

pygame.init()
pygame.display.set_caption("Connect Four!")

WIN = pygame.display.set_mode((900, 600))
BOARD = pygame.Rect(100, 0, 700, 600)
board = pygame.Surface((700, 600))
restartColumn = pygame.Rect(0, 0, 100, 600)
column1 = pygame.Rect(100, 0, 100, 600)
column2 = pygame.Rect(200, 0, 100, 600)
column3 = pygame.Rect(300, 0, 100, 600)
column4 = pygame.Rect(400, 0, 100, 600)
column5 = pygame.Rect(500, 0, 100, 600)
column6 = pygame.Rect(600, 0, 100, 600)
column7 = pygame.Rect(700, 0, 100, 600)
quitColumn = pygame.Rect(800, 0, 100, 600)

font = pygame.font.SysFont("impact", 50)
redWinText = font.render("The winner is Red! Play again?", False, (0, 0, 0))
yellowWinText = font.render("The winner is Yellow! Play again?", False, (0, 0, 0))
noWinText = font.render("No winner... Play again?", False, (0, 0, 0))
yesText = font.render("YES", False, (255, 255, 255))
noText = font.render("NO", False, (255, 255, 255))

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


def isFinished(currentBoard):
    #from top left to bottom right, starting on left side
    diag1 = [currentBoard[1][3], currentBoard[2][2], currentBoard[3][1], currentBoard[4][0]]
    diag2 = [currentBoard[1][4], currentBoard[2][3], currentBoard[3][2], currentBoard[4][1], currentBoard[5][0]]
    diag3 = [currentBoard[1][5], currentBoard[2][4], currentBoard[3][3], currentBoard[4][2], currentBoard[5][1], currentBoard[6][0]]
    diag4 = [currentBoard[2][5], currentBoard[3][4], currentBoard[4][3], currentBoard[5][2], currentBoard[6][1], currentBoard[7][0]]
    diag5 = [currentBoard[3][5], currentBoard[4][4], currentBoard[5][3], currentBoard[6][2], currentBoard[7][1]]
    diag6 = [currentBoard[4][5], currentBoard[5][4], currentBoard[6][3], currentBoard[7][2]]
    #from bottom left to top right, starting on left side
    diag7 = [currentBoard[1][2], currentBoard[2][3], currentBoard[3][4], currentBoard[4][5]]
    diag8 = [currentBoard[1][1], currentBoard[2][2], currentBoard[3][3], currentBoard[4][4], currentBoard[5][5]]
    diag9 = [currentBoard[1][0], currentBoard[2][1], currentBoard[3][2], currentBoard[4][3], currentBoard[5][4], currentBoard[6][5]]
    diag10 = [currentBoard[2][0], currentBoard[3][1], currentBoard[4][2], currentBoard[5][3], currentBoard[6][4], currentBoard[7][5]]
    diag11 = [currentBoard[3][0], currentBoard[4][1], currentBoard[5][2], currentBoard[6][3], currentBoard[7][4]]
    diag12 = [currentBoard[4][0], currentBoard[5][1], currentBoard[6][2], currentBoard[7][3]]
    #from left to right, starting on top
    row1 = [currentBoard[1][5], currentBoard[2][5], currentBoard[3][5], currentBoard[4][5], currentBoard[5][5], currentBoard[6][5], currentBoard[7][5]]
    row2 = [currentBoard[1][4], currentBoard[2][4], currentBoard[3][4], currentBoard[4][4], currentBoard[5][4], currentBoard[6][4], currentBoard[7][4]]
    row3 = [currentBoard[1][3], currentBoard[2][3], currentBoard[3][3], currentBoard[4][3], currentBoard[5][3], currentBoard[6][3], currentBoard[7][3]]
    row4 = [currentBoard[1][2], currentBoard[2][2], currentBoard[3][2], currentBoard[4][2], currentBoard[5][2], currentBoard[6][2], currentBoard[7][2]]
    row5 = [currentBoard[1][1], currentBoard[2][1], currentBoard[3][1], currentBoard[4][1], currentBoard[5][1], currentBoard[6][1], currentBoard[7][1]]
    row6 = [currentBoard[1][0], currentBoard[2][0], currentBoard[3][0], currentBoard[4][0], currentBoard[5][0], currentBoard[6][0], currentBoard[7][0]]

    possibleWinLanes = [row1, diag1, diag2, diag3, diag4, diag5, diag6, diag7, diag8, diag9, diag10, diag11, diag12, row2, row3, row4, row5, row6, currentBoard[1], currentBoard[2], currentBoard[3], currentBoard[4], currentBoard[5], currentBoard[6], currentBoard[7]]

    full = 1
    
    for lane in possibleWinLanes: #checking all win lanes for 4 similar pieces in a row
        if "X" in lane:
            full = 0
        for i in range(len(lane[:-3])):
            if lane[i] + lane[i+1] + lane[i+2] + lane[i+3] == "YYYY":
                return "Yellow"
            elif lane[i] + lane[i+1] + lane[i+2] + lane[i+3] == "RRRR":
                return "Red"
            elif full == 1:
                return "Tie"
    return False

currentBoard = {1:"XXXXXX", 2:"XXXXXX", 3:"XXXXXX", 4:"XXXXXX", 5:"XXXXXX", 6:"XXXXXX", 7:"XXXXXX"}

def formatColumns(column, playercolor): #formatting columns so they can be read for isFinished()
    stop = 0
    for index, char in enumerate(currentBoard[column]):
        if char == "X" and stop == 0:
            currentBoard[column] = currentBoard[column][:index] + playercolor + currentBoard[column][index+1:]
            currentBoard[column] = currentBoard[column][:6]
            stop = 1

def Connect4(): #main loop
    run = True
    drawBoard()
    player = 1
    c1count = 0
    c2count = 0
    c3count = 0
    c4count = 0
    c5count = 0
    c6count = 0
    c7count = 0

    redRect = redWinText.get_rect()
    redRect.center = ((450, 300))
    yellowRect = yellowWinText.get_rect()
    yellowRect.center = ((450, 300))
    noWinRect = noWinText.get_rect()
    noWinRect.center = ((450, 300))
    yesRect = yesText.get_rect()
    yesRect.center = ((50, 300))
    noRect = noText.get_rect()
    noRect.center = ((850, 300))
    
    while run:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePosition = pygame.mouse.get_pos()
                if column1.collidepoint(mousePosition):
                    if player == 1 and c1count < 6:
                        pygame.draw.circle(WIN, (255, 0, 0), (150, (550 - 100*c1count)), 40)
                        c1count += 1
                        formatColumns(1, "R")
                        player = 2
                        yesRect.center = ((1000, 1000))
                    elif c1count < 6:
                        pygame.draw.circle(WIN, (255, 255, 0), (150, (550 - 100*c1count)), 40)
                        c1count += 1
                        formatColumns(1, "Y")
                        player = 1
                        
                if column2.collidepoint(mousePosition):
                    if player == 1 and c2count < 6:
                        pygame.draw.circle(WIN, (255, 0, 0), (250, (550 - 100*c2count)), 40)
                        c2count += 1
                        formatColumns(2, "R")
                        player = 2
                    elif c2count < 6:
                        pygame.draw.circle(WIN, (255, 255, 0), (250, (550 - 100*c2count)), 40)
                        c2count += 1
                        formatColumns(2, "Y")
                        player = 1
                        
                if column3.collidepoint(mousePosition):
                    if player == 1 and c3count < 6:
                        pygame.draw.circle(WIN, (255, 0, 0), (350, (550 - 100*c3count)), 40)
                        c3count += 1
                        formatColumns(3, "R")
                        player = 2
                    elif c3count < 6:
                        pygame.draw.circle(WIN, (255, 255, 0), (350, (550 - 100*c3count)), 40)
                        c3count += 1
                        formatColumns(3, "Y")
                        player = 1

                if column4.collidepoint(mousePosition):
                    if player == 1 and c4count < 6:
                        pygame.draw.circle(WIN, (255, 0, 0), (450, (550 - 100*c4count)), 40)
                        c4count += 1
                        formatColumns(4, "R")
                        player = 2
                    elif c4count < 6:
                        pygame.draw.circle(WIN, (255, 255, 0), (450, (550 - 100*c4count)), 40)
                        c4count += 1
                        formatColumns(4, "Y")
                        player = 1

                if column5.collidepoint(mousePosition):
                    if player == 1 and c5count < 6:
                        pygame.draw.circle(WIN, (255, 0, 0), (550, (550 - 100*c5count)), 40)
                        c5count += 1
                        formatColumns(5, "R")
                        player = 2
                    elif c5count < 6:
                        pygame.draw.circle(WIN, (255, 255, 0), (550, (550 - 100*c5count)), 40)
                        c5count += 1
                        formatColumns(5, "Y")
                        player = 1

                if column6.collidepoint(mousePosition):
                    if player == 1 and c6count < 6:
                        pygame.draw.circle(WIN, (255, 0, 0), (650, (550 - 100*c6count)), 40)
                        c6count += 1
                        formatColumns(6, "R")
                        player = 2
                    elif c6count < 6:
                        pygame.draw.circle(WIN, (255, 255, 0), (650, (550 - 100*c6count)), 40)
                        c6count += 1
                        formatColumns(6, "Y")
                        player = 1

                if column7.collidepoint(mousePosition):
                    if player == 1 and c7count < 6:
                        pygame.draw.circle(WIN, (255, 0, 0), (750, (550 - 100*c7count)), 40)
                        c7count += 1
                        formatColumns(7, "R")
                        player = 2
                    elif c7count < 6:
                        pygame.draw.circle(WIN, (255, 255, 0), (750, (550 - 100*c7count)), 40)
                        c7count += 1
                        formatColumns(7, "Y")
                        player = 1
                        
                if isFinished(currentBoard) != False:
                    if restartColumn.collidepoint(mousePosition):
                        restart(currentBoard)
                    if quitColumn.collidepoint(mousePosition):
                        run = False
                        break

        winner = isFinished(currentBoard)
        if winner != False: #displays winner and asks to play again?
            if winner == "Yellow":
                WIN.blit(yesText, yesRect)
                WIN.blit(yellowWinText, yellowRect)
                WIN.blit(noText, noRect)
            elif winner == "Red":
                WIN.blit(redWinText, redRect)
                WIN.blit(yesText, yesRect)
                WIN.blit(noText, noRect)
            elif winner == "Tie":
                WIN.blit(noWinText, noWinRect)
                WIN.blit(yesText, yesRect)
                WIN.blit(noText, noRect)
        
    pygame.quit()

def restart(currentBoard): #restarts game
    currentBoard[1] = "XXXXXX"
    currentBoard[2] = "XXXXXX"
    currentBoard[3] = "XXXXXX"
    currentBoard[4] = "XXXXXX"
    currentBoard[5] = "XXXXXX"
    currentBoard[6] = "XXXXXX"
    currentBoard[7] = "XXXXXX"
    WIN.fill((0, 0, 0))
    Connect4()
    
Connect4()
