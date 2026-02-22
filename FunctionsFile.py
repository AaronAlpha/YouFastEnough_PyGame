import pygame
import random as r

import ButtonsClass as buttons

def draw_text(screen, text, font, textColor, x, y):    
    textIMG = font.render(text, True, textColor)
    screen.blit(textIMG, (x, y))
    
def displayTextRandomizerEasy():
    list1 = []    
    for i in range(5):
        list1.append( str(r.randint(0, 9)) )
    return list1

def displayTextRandomizerMedium():
    list1 = []
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(6):
        list1.append(r.randint(0, 51))
    SelectedAlpabetsList = [] # all randomly choosen alphabets
    for i in list1:
        SelectedAlpabetsList += [alphabets[i]]
    return SelectedAlpabetsList

def displayTextRandomizerHard():
    list1 = [] # num
    list2 = [] # alphabets
    listR = [] # alphanumeric list
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "0", "1", "2", "3", "4", "5", "6", "7", "8" ,"9"]
    for i in range(7):
        list1.append(r.randint(0, 61))
    for i in list1:
        listR.append(alphabets[i])
    return listR

def gameOver(screen, textFont1, textFont2, HighestScore, num, screenWidth, screenHeight):
    # button definition
    playAgain = buttons.Buttons(0.1*screenWidth + (0.1*screenWidth/2) + 40, 5*(0.1*screenHeight + 10) + 30,"Play Again", 40,200, 100, (255, 255, 255))
    exitButton = buttons.Buttons(4*(0.1*screenWidth + (0.1*screenWidth/2) )-40, 5*(0.1*screenHeight + 10) + 30,"Exit", 50,200, 100, (255, 255, 255))
    
    pygame.draw.rect(screen, (0,0 ,0) ,(0.1*screenWidth, 0.1*screenHeight, screenWidth - (2*(0.1*screenWidth)), screenHeight - (2*(0.1*screenHeight)) ) )
   
    # Game Over
    draw_text(screen, "Game Over", textFont1, (255, 255, 255 ), 0.1*screenWidth + (0.1*screenWidth), 0.1*screenHeight +10 )
    
    # High Score Display
    draw_text(screen, "Score: " + str(HighestScore) + " (correct=+10)", textFont2, (255, 255, 255 ), 0.1*screenWidth + (0.1*screenWidth/2) - 20,  3*(0.1*screenHeight + 10) )
    
    # Levels
    draw_text(screen, "Number of Attempts: " + str(num), textFont2, (255, 255, 255 ), 0.1*screenWidth + (0.1*screenWidth/2) - 20,  4*(0.1*screenHeight + 10))
    
    # Play Again button
    if playAgain.draw(screen):
        return True # True that 'Play Again' was hit
    if exitButton.draw(screen):
        return False # False that 'Play Again' was not hit
    # Exit Button
    