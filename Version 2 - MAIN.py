import pygame

import FunctionsFile as func
import ButtonsClass as buttons

# %% Setup

pygame.init()

screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode( (screenWidth, screenHeight ) )

pygame.display.set_caption("Game Window")

# %% Game Veriables
screenListColor = {"menu": (137, 207, 240), "easyGame": ( 224, 17, 95 ), "mediumGame": ( 15, 82, 186), "hardGame": ( 80, 220, 100), "gameOver":(0, 0, 0)}
black = (0, 0, 0)
orange = (255, 68, 51)

red = (240, 0, 90)
yellow = (255, 255, 0)
orange2 = (255, 69, 0)
inputColor = (0, 0, 0)

# game instructions:
line1 = "Instructions:"

line2 = "-Press the button of your"
line2b = "desired 'Play Level'"

line3 = "-Memorize and enter the"
line3b = "list of numbers that flash"
line3c = "on the screen before the"
line3d = "timer runs out."

line4 = "-You can use 'Hints', when"
line4b = "stuck, to get a brief glimpse"
line4c = "at the list of numbers"
line4d = "or letters or both!"

line5 = "-Try beating your High"
line5b = "Score and Good Luck!"
    
# text stuff
fontSizes = {
    "instrucTitle": 60,
    "instrucLines": 40,
    "gameName": 100,
    "inputText": 70,
    "hintText": 20,
    "gameOver": 80
    }

textFontGameName = pygame.font.Font("TechnoRaceItalic-eZRWe.otf", fontSizes["gameName"]) 
textFontNames = pygame.font.SysFont(None, fontSizes["instrucLines"]) 

textFontChoosePlay = pygame.font.SysFont(None, fontSizes["instrucLines"]) 

textFontInstructionTitle = pygame.font.SysFont(None, fontSizes["instrucTitle"]) 
textFontInstructionLines = pygame.font.SysFont(None, fontSizes["instrucLines"]) 

textFontInputText = pygame.font.SysFont(None, fontSizes["inputText"]) 
hintText = pygame.font.Font("TechnoRaceItalic-eZRWe.otf", fontSizes["hintText"]) 

textFontGameOver = pygame.font.SysFont(None, fontSizes["gameOver"]) 

# Game Timer
timer = {
    "easyTime": 15,
    "mediumTime": 10,
    "hardTime": 5
    }
timeSlept = False
timerEasy = 1500
tempTimeEasy = 200
timerMedium = 1000
tempTimeMedium = 200
timerHard = 500
tempTimeHard = 200

# Game input string
displayTextEasy = [[], "[?, ?, ?, ?, ?]"]
displayTextMedium = [[], "[?, ?, ?, ?, ?, ?]"]
displayTextHard = [[], "[?, ?, ?, ?, ?, ?, ?]"]
inputText = ""
inputTextList = []

# Game Mechanics Vars
tempScore = [0, 0, 0]
storedScores = [0, 0, 0]
HighestScore = 0    
numAttempts = [0, 0, 0] # for how many times the user successfully entered the correct entry within the time limit


# %% Game States
# states: "menu", "easyGame", "mediumGame", "hardGame", "gameOver"
game_state = "menu"

# gameplay start state:
start_state = "not started"

toHint = "no hint"

nextOne = "no"

# %% Game Buttons

# Menu
playEasy = buttons.Buttons(20, 130 + 80, "Play - Easy Mode", 30, 300 + 60, 50, red)


playMedium = buttons.Buttons(20, 130 + 80 + 55, "Play - Medium Mode", 30, 300 + 60, 50, yellow)

playHard = buttons.Buttons(20, 130 + 80 + 55 + 55, "Play - Hard Mode", 30, 300 + 60, 50, orange2)


# %% Game time

clock = pygame.time.Clock()



# %% Game Run
gameRun = True
while gameRun:
    # screens
    if game_state == "menu":
        screen.fill(screenListColor[game_state])
        
        pygame.draw.rect(screen , black, (20, 20, screenWidth - 40, 100), width = 5)
        func.draw_text(screen, "You Fast Enough?", textFontGameName, orange, 20 + 5 +10, 20)
        
        func.draw_text(screen, "Choose one of the three", textFontChoosePlay, black,20, 130 + 5)
        func.draw_text(screen, "difficualty levels:", textFontChoosePlay, black,20, 160 + 5)

        # instruction display
        pygame.draw.rect(screen , black, (screenWidth/2, 130, screenWidth/2 - 20, screenHeight - 40 - 110), width = 5)
        
        func.draw_text(screen, line1, textFontInstructionTitle, black ,screenWidth/2 + 5, 130 + 5)
        
        func.draw_text(screen, line2, textFontInstructionLines, black ,screenWidth/2 + 5, 130 + 50)
        func.draw_text(screen, line2b, textFontInstructionLines, black ,screenWidth/2 + 5, 130 + 80)
        
        func.draw_text(screen, line3, textFontInstructionLines, black ,screenWidth/2 + 5, 130 + 120)
        func.draw_text(screen, line3b, textFontInstructionLines, black ,screenWidth/2 + 5, 130 + 150)
        func.draw_text(screen, line3c, textFontInstructionLines, black ,screenWidth/2 + 5, 130 + 180)
        func.draw_text(screen, line3d, textFontInstructionLines, black ,screenWidth/2 + 5, 130 + 210)
        
        func.draw_text(screen, line4, textFontInstructionLines, black ,screenWidth/2 + 5, 130 + 250)
        func.draw_text(screen, line4b, textFontInstructionLines, black ,screenWidth/2 + 5, 130 + 280)
        func.draw_text(screen, line4c, textFontInstructionLines, black ,screenWidth/2 + 5, 130 + 310)
        func.draw_text(screen, line4d, textFontInstructionLines, black ,screenWidth/2 + 5, 130 + 340)
        
        func.draw_text(screen, line5, textFontInstructionLines, black, screenWidth/2 + 5, 130 + 380)
        func.draw_text(screen, line5b, textFontInstructionLines, black ,screenWidth/2 + 5, 130 + 410)
        
        if playEasy.draw(screen):
            game_state = "easyGame"
            
        elif playMedium.draw(screen):
            game_state = "mediumGame"
            
        elif playHard.draw(screen):
            game_state = "hardGame"
        
        
        
        func.draw_text(screen, "Highest Score: " + str(HighestScore), textFontChoosePlay, black,20 +50 + 20, 130 + 80 + 55 + 55 + 100 + 50)
        

# %% Easy game part
    elif game_state == "easyGame":
        screen.fill(screenListColor[game_state])
        
        if len(displayTextEasy[0]) == 0:
            displayTextEasy[0] = func.displayTextRandomizerEasy()
        
        backButton = buttons.Buttons(0.05*screenWidth, 100 ,"Menu", 40,200, 50, (255, 255, 255))
        if backButton.draw(screen):
            game_state = "menu"
            start_state = "not started"
            timerEasy = 1500
            tempScore[0] = 0
        
        func.draw_text(screen, "Score: " + str(tempScore[0]) , textFontInputText, (0,0,0), 0.05*screenWidth, 30 )
        
        func.draw_text(screen, "Timer: " + str( int(timerEasy/100 ) ), textFontInputText, (0, 0, 0 ), screenWidth/2 - 100-10, 30 )  
        
        hints = buttons.Buttons(screenWidth - .1*screenWidth - 150, 100 ,"Hints", 40,200, 50, (255, 255, 255))
        if hints.draw(screen):
            nextOne = "next"
        
        # start button
        startButton = buttons.Buttons(screenWidth/2 - 100, 100 ,"Start", 40,200, 50, (255, 255, 255))
        if startButton.draw(screen):
            start_state = "started"
        
        if nextOne == "next":
            pygame.draw.rect(screen, (0, 0, 0), (screenWidth/2 - 100 - 50 - 100 - 50, 3*(0.1*screenHeight), 600, 80 + 10), width = 5)
            func.draw_text(screen, str(displayTextEasy[0]), textFontInputText, (106, 13, 173), screenWidth/2 - 100 - 50 + 20 - 60, 3*(0.1*screenHeight) + 10)
            tempTimeEasy -= 1
            if tempTimeEasy == 0:
                nextOne = "no"
                tempTimeEasy = 200
        
        if start_state == "not started":
            pygame.draw.rect(screen, (0, 0, 0), (screenWidth/2 - 100 - 50 - 100 - 50, 3*(0.1*screenHeight), 600, 80 + 10), width = 5)
            func.draw_text(screen, str(displayTextEasy[0]), textFontInputText, (106, 13, 173), screenWidth/2 - 100 - 50 + 20 - 60, 3*(0.1*screenHeight) + 10)
            
        elif start_state == "started":
            timerEasy -= 1
            if nextOne == "no":
                pygame.draw.rect(screen, (0, 0, 0), (screenWidth/2 - 100 - 50 - 100 - 50, 3*(0.1*screenHeight), 600, 80 + 10), width = 5)
                func.draw_text(screen, displayTextEasy[1], textFontInputText, (106, 13, 173), 300 - 20 , 3*(0.1*screenHeight) + 10)
                
            pygame.draw.rect(screen, inputColor, (screenWidth/2 - 100 - 50 - 100 - 50, 7*(0.1*screenHeight), 600, 80 + 10), width = 5)
            func.draw_text(screen, inputText, textFontInputText, (106, 13, 173), 300 - 20, 7*(0.1*screenHeight) + 10)            
            
        # End Game - timer = 0
        if timerEasy == 0:
            start_state = "not started"
            nextOne = "no"
            storedScores[0] = tempScore[0]
            
            if func.gameOver(screen, textFontGameName, textFontGameOver, tempScore[0], numAttempts[0], screenWidth, screenHeight) == True:
                game_state = "menu"
                timerEasy = 1500
                displayTextEasy[0] = []
                levels = 0
                tempScore[0] = 0
                inputText = ""
                inputTextList = []
                
            elif func.gameOver(screen, textFontGameName, textFontGameOver, tempScore[0], numAttempts[0], screenWidth, screenHeight) == False:
                gameRun = False
            
# %% Medium game part
    elif game_state == "mediumGame":
        screen.fill(screenListColor[game_state])
        
        if len(displayTextMedium[0]) == 0:
            displayTextMedium[0] = func.displayTextRandomizerMedium()
        
        backButton = buttons.Buttons(0.05*screenWidth, 100 ,"Menu", 40,200, 50, (255, 255, 255))
        if backButton.draw(screen):
            game_state = "menu"
            start_state = "not started"
            timerMedium = 1000
            tempScore[1] = 0
        
        func.draw_text(screen, "Score: " + str(tempScore[1]) , textFontInputText, (0,0,0), 0.05*screenWidth, 30 )
        
        func.draw_text(screen, "Timer: " + str( int(timerMedium/100 ) ), textFontInputText, (0, 0, 0 ), screenWidth/2 - 100-10, 30 )
        
        hints = buttons.Buttons(screenWidth - .1*screenWidth - 150, 100 ,"Hints", 40,200, 50, (255, 255, 255))
        if hints.draw(screen):
           nextOne = "next"

        # start button
        startButton = buttons.Buttons(screenWidth/2 - 100, 100 ,"Start", 40,200, 50, (255, 255, 255))
        if startButton.draw(screen):
            start_state = "started"
        
        if nextOne == "next":
            pygame.draw.rect(screen, (0, 0, 0), (screenWidth/2 - 100 - 50 - 100 - 50, 3*(0.1*screenHeight), 600, 80 + 10), width = 5)
            
            func.draw_text(screen, str(displayTextMedium[0]), textFontInputText, (255, 215, 0), screenWidth/2 - 100 - 50 + 20 - 80, 3*(0.1*screenHeight) + 10)
            tempTimeMedium -= 1
            if tempTimeMedium == 0:
                nextOne = "no"
                tempTimeMedium = 200
            
        if start_state == "not started":
            pygame.draw.rect(screen, (0, 0, 0), (screenWidth/2 - 100 - 50 - 100 - 50, 3*(0.1*screenHeight), 600, 80 + 10), width = 5)
            
            func.draw_text(screen, str(displayTextMedium[0]), textFontInputText, (255, 215, 0), screenWidth/2 - 100 - 50 + 20 - 80, 3*(0.1*screenHeight) + 10)
            
        elif start_state == "started":
            timerMedium -= 1
            
            if nextOne == "no":
                pygame.draw.rect(screen, (0, 0, 0), (screenWidth/2 - 100 - 50 - 100 - 50, 3*(0.1*screenHeight), 600, 80 + 10), width = 5)    
                func.draw_text(screen, displayTextMedium[1], textFontInputText, (255, 215, 0), 300 - 20 - 60, 3*(0.1*screenHeight) + 10)
            
            pygame.draw.rect(screen, inputColor, (screenWidth/2 - 100 - 50 - 100 - 50, 7*(0.1*screenHeight), 600, 80 + 10), width = 5)
            func.draw_text(screen, inputText, textFontInputText, (255, 215, 0), 300 - 20, 7*(0.1*screenHeight) + 10)
        
        # End Game - timer = 0
        if timerMedium == 0:
            start_state = "not started"
            nextOne = "no"
            storedScores[1] = tempScore[1]
            
            if func.gameOver(screen, textFontGameName, textFontGameOver, tempScore[1], numAttempts[1], screenWidth, screenHeight) == True:
                game_state = "menu"
                timerMedium = 1000
                displayTextMedium[0] = []
                levels = 0
                tempScore[1] = 0
                inputText = ""
                inputTextList = []
            elif func.gameOver(screen, textFontGameName, textFontGameOver, tempScore[1], numAttempts[1], screenWidth, screenHeight) == False:
                gameRun = False
        
# %% Hard game part
    elif game_state == "hardGame":
        screen.fill(screenListColor[game_state])
        
        if len(displayTextHard[0]) == 0:
            displayTextHard[0] = func.displayTextRandomizerHard()
        
        # back button
        backButton = buttons.Buttons(0.05*screenWidth, 100 ,"Menu", 40,200, 50, (255, 255, 255))
        if backButton.draw(screen):
            game_state = "menu"
            start_state = "not started"
            timerHard = 1500
            tempScore[2] = 0
        
        func.draw_text(screen, "Score: " + str(tempScore[2]) , textFontInputText, (0,0,0), 0.05*screenWidth, 30 )
        
        func.draw_text(screen, "Timer: " + str( int(timerHard/100 ) ), textFontInputText, (0, 0, 0 ), screenWidth/2 - 100-10, 30 )
        
        hints = buttons.Buttons(screenWidth - .1*screenWidth - 150, 100 ,"Hints", 40,200, 50, (255, 255, 255))
        if hints.draw(screen):
           nextOne = "next"

        # start button
        startButton = buttons.Buttons(screenWidth/2 - 100, 100 ,"Start", 40,200, 50, (255, 255, 255))
        if startButton.draw(screen):
            start_state = "started"        
        
        if nextOne == "next":
            pygame.draw.rect(screen, (0, 0, 0), (screenWidth/2 - 100 - 50 - 100 - 50, 3*(0.1*screenHeight), 600, 80 + 10), width = 5)
            func.draw_text(screen, str(displayTextHard[0]), textFontInputText, (106, 13, 173), screenWidth/2 - 100 - 50 + 20 - 120, 3*(0.1*screenHeight) + 10)
            tempTimeHard -= 1
            if tempTimeHard == 0:
                nextOne = "no"
                tempTimeHard = 200
        
        if start_state == "not started":
            pygame.draw.rect(screen, (0, 0, 0), (screenWidth/2 - 100 - 50 - 100 - 50, 3*(0.1*screenHeight), 600, 80 + 10), width = 5)
            
            func.draw_text(screen, str(displayTextHard[0]), textFontInputText, (106, 13, 173), screenWidth/2 - 100 - 50 + 20 - 120, 3*(0.1*screenHeight) + 10)
    
        elif start_state == "started" :
            timerHard -= 1
            
            if nextOne == "no":
                pygame.draw.rect(screen, (0, 0, 0), (screenWidth/2 - 100 - 50 - 100 - 50, 3*(0.1*screenHeight), 600, 80 + 10), width = 5)
                
                func.draw_text(screen, displayTextHard[1], textFontInputText, (106, 13, 173), 300 - 20 - 80, 3*(0.1*screenHeight) + 10)
            
            pygame.draw.rect(screen, inputColor, (screenWidth/2 - 100 - 50 - 100 - 50, 7*(0.1*screenHeight), 600, 80 + 10), width = 5)
            
            func.draw_text(screen, inputText, textFontInputText, (106, 13, 173), 300 - 20, 7*(0.1*screenHeight) + 10)
        
        # End Game - timer = 0
        if timerHard == 0:
            start_state = "not started"
            nextOne = "no"
            storedScores[2] = tempScore[2]
            
            if func.gameOver(screen, textFontGameName, textFontGameOver, tempScore[2], numAttempts[2], screenWidth, screenHeight) == True:
                game_state = "menu"
                timerHard = 500        
                displayTextMedium[0] = []
                levels = 0
                tempScore[2] = 0
                inputText = ""
                inputTextList = []
            elif func.gameOver(screen, textFontGameName, textFontGameOver, tempScore[2], numAttempts[2], screenWidth, screenHeight) == False:
                gameRun = False
            

# Menu Code
    # title
    # event handler
    for event in pygame.event.get():
        # quit
        if event.type == pygame.QUIT:
            gameRun = False
            
        # text input
        if not(timerEasy == 0 or timerMedium == 0 or timerHard == 0 ):
            if event.type == pygame.TEXTINPUT:
                inputText += " " + event.text
                inputTextList.append( (event.text) )
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    inputText = inputText[:-1]
                    inputTextList.pop()
                    print(inputTextList)
                    
                if event.key == pygame.K_RETURN:
                    if game_state == "easyGame":
                        if displayTextEasy[0] == inputTextList:
                            inputColor = (0, 255, 0)
                            tempScore[0] += 10
                            numAttempts[0] += 1
                            displayTextEasy[0] = []
                            inputText = ""
                            inputTextList = []
                            timerEasy += 500
                            nextOne = "next"
                        else:
                            inputColor = (255, 0, 0)
                            inputText = ""
                            inputTextList = []
                            numAttempts[0] += 1
                    
                    elif game_state == "mediumGame":
                        if displayTextMedium[0] == inputTextList:
                            inputColor = (0, 255, 0)
                            tempScore[1] += 10
                            numAttempts[1] += 1
                            displayTextMedium[0] = []
                            inputText = ""
                            inputTextList = []
                            timerMedium += 500
                            nextOne = "next"
                        else:
                            inputColor = (255, 0, 0)
                            inputText = ""
                            inputTextList = []
                            numAttempts[1] += 1
                    
                    elif game_state == "hardGame":
                        if displayTextHard[0] == inputTextList:
                            inputColor = (0, 255, 0)
                            tempScore[2] += 10
                            numAttempts[2] += 1
                            displayTextHard[0] = []
                            inputText = ""
                            inputTextList = []
                            timerHard += 500
                            nextOne = "next"
                        else:
                            inputColor = (255, 0, 0)
                            inputText = ""
                            inputTextList = []
                            numAttempts[2] += 1
                            
    HighestScore = storedScores[0]
    for i in range(len(storedScores)):
        if storedScores[i] > HighestScore:
            HighestScore = storedScores[i]
        
    # screen update
    pygame.display.update()
    clock.tick(100)

pygame.quit()   
