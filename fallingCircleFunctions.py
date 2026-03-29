from datetime import time
import tkinter as tk
from tkinter import messagebox
import gamePanel
import main

# Variables to track the movement of the falling circles
isLargeCircle1MovingDown = False
isSmallCircle1MovingDown = False
isLargeCircle2MovingDown = False
isSmallCircle2MovingDown = False
isLargeCircle3MovingDown = False
isSmallCircle3MovingDown = False
isGameRunning = False
isPlayerLost = False
animationRunning = None

# Functions to start and stop the movement of the falling circles
def LargeCircle1MovingDown():
    global isLargeCircle1MovingDown
    isLargeCircle1MovingDown = True

def largeCircle1StopMovingDown():
    global isLargeCircle1MovingDown
    isLargeCircle1MovingDown = False

def smallCircle1MovingDown():
    global isSmallCircle1MovingDown
    isSmallCircle1MovingDown = True

def smallCircle1StopMovingDown():
    global isSmallCircle1MovingDown
    isSmallCircle1MovingDown = False

def largeCircle2MovingDown():
    global isLargeCircle2MovingDown
    isLargeCircle2MovingDown = True

def largeCircle2StopMovingDown():
    global isLargeCircle2MovingDown
    isLargeCircle2MovingDown = False

def smallCircle2MovingDown():
    global isSmallCircle2MovingDown
    isSmallCircle2MovingDown = True

def smallCircle2StopMovingDown():
    global isSmallCircle2MovingDown
    isSmallCircle2MovingDown = False

def largeCircle3MovingDown():
    global isLargeCircle3MovingDown
    isLargeCircle3MovingDown = True

def largeCircle3StopMovingDown():
    global isLargeCircle3MovingDown
    isLargeCircle3MovingDown = False

def smallCircle3MovingDown():
    global isSmallCircle3MovingDown
    isSmallCircle3MovingDown = True

def smallCircle3StopMovingDown():
    global isSmallCircle3MovingDown
    isSmallCircle3MovingDown = False

def playerIsNotLost():
    global isPlayerLost
    isPlayerLost = False

def playerIsLost():
    global isPlayerLost
    isPlayerLost = True

# Functions to start and stop the game
def gameIsRunning():
    global isGameRunning
    isGameRunning = True

def gameIsNotRunning():
    global isGameRunning
    isGameRunning = False

# Function to move the falling circles down by a specified amount
def moveTheCirclesDown():
    global isGameRunning
    global animationRunning
    gameIsRunning()

    if isGameRunning:
        if playerIsLost():
            return
        else:
            # Move the falling circles down by 5 pixels if they are currently moving down
            LargeCircle1MovingDown()
            smallCircle1MovingDown()
            largeCircle2MovingDown()
            smallCircle2MovingDown()
            largeCircle3MovingDown()
            smallCircle3MovingDown()
            if isLargeCircle1MovingDown:
                gamePanel.canvasShooter.move(gamePanel.largeFallingCircle1, 0, 0.75)
                circleContactWithShotRectangle()
            if isSmallCircle1MovingDown:
                gamePanel.canvasShooter.move(gamePanel.smallFallingCircle1, 0, 0.75)
                circleContactWithShotRectangle()
            if isLargeCircle2MovingDown:
                gamePanel.canvasShooter.move(gamePanel.largeFallingCircle2, 0, 0.5)
                circleContactWithShotRectangle()
            if isSmallCircle2MovingDown:
                gamePanel.canvasShooter.move(gamePanel.smallFallingCircle2, 0, 0.75)
                circleContactWithShotRectangle()
            if isLargeCircle3MovingDown:
                gamePanel.canvasShooter.move(gamePanel.largeFallingCircle3, 0, 0.5)
                circleContactWithShotRectangle()
            if isSmallCircle3MovingDown:
                gamePanel.canvasShooter.move(gamePanel.smallFallingCircle3, 0, 0.75)
                circleContactWithShotRectangle()

        # Check if the player has lost and stop moving the circles down if they have, otherwise continue moving the circles down
        playerLoses()
        if playerLoses():
            return
        else:
            animationRunning = gamePanel.canvasShooter.after(16, moveTheCirclesDown)
        


def playerLoses():
    global isGameRunning
    # Get the height of the shooter canvas
    shooterCanvasHeight = gamePanel.canvasShooter.winfo_height()

    # Get the coordinates of the falling circles
    xLF1, yLF1, xLF2, yLF2 = gamePanel.canvasShooter.coords(gamePanel.largeFallingCircle1)
    xSF1, ySF1, xSF2, ySF2 = gamePanel.canvasShooter.coords(gamePanel.smallFallingCircle1)
    xLS1, yLS1, xLS2, yLS2 = gamePanel.canvasShooter.coords(gamePanel.largeFallingCircle2)
    xSS1, ySS1, xSS2, ySS2 = gamePanel.canvasShooter.coords(gamePanel.smallFallingCircle2)
    xLT1, yLT1, xLT2, yLT2 = gamePanel.canvasShooter.coords(gamePanel.largeFallingCircle3)
    xST1, yST1, xST2, yST2 = gamePanel.canvasShooter.coords(gamePanel.smallFallingCircle3)

    # Check if any of the falling circles have reached the bottom of the canvas
    if any([yLF2 > shooterCanvasHeight, ySF2 > shooterCanvasHeight, yLS2 > shooterCanvasHeight, ySS2 > shooterCanvasHeight, yLT2 > shooterCanvasHeight, yST2 > shooterCanvasHeight]):
        # If the player has lost, stop moving the circles down and reset their positions
        playerIsLost()
        isGameRunning = False
        resetLargeCircle1()
        resetSmallCircle1()
        resetLargeCircle2()
        resetSmallCircle2()
        resetLargeCircle3()
        resetSmallCircle3()
        largeCircle1StopMovingDown()
        smallCircle1StopMovingDown()
        largeCircle2StopMovingDown()
        smallCircle2StopMovingDown()
        largeCircle3StopMovingDown()
        smallCircle3StopMovingDown()
        backToTitlePanelIfLost()
        return True
    else:
        # If the player has not lost, continue moving the circles down
        playerIsNotLost()
    return False

def backToTitlePanelIfLost():
    # If the player has lost, display a message box and return to the title panel if they choose to
    global isGameRunning
    global animationRunning
    if animationRunning is not None:
        gamePanel.canvasShooter.after_cancel(animationRunning)
        animationRunning = None
    
    isGameRunning = False 
    

    exitGameMessage = messagebox.askyesno("Game Over", "You lost! Return to title?")

    if exitGameMessage:
        # Reset the game panel and return to the title panel
        gamePanel.resetGamePanel()  
        main.openTitlePanel(root=main.main.__globals__['root'])
        main.isTitlePanelOpen = True
        while main.isTitlePanelOpen == True:
            resetLargeCircle1()
            resetSmallCircle1()
            resetLargeCircle2()
            resetSmallCircle2()
            resetLargeCircle3()
            resetSmallCircle3()
            time.sleep(0.1)
    else:
        # Reset the positions of the falling circles and start moving them down again
        resetLargeCircle1()
        resetSmallCircle1() 
        isGameRunning = True 
        moveTheCirclesDown() 



def circleContactWithShotRectangle():
    # Get the coordinates of the shot rectangle
    xR1, yR1, xR2, yR2 = gamePanel.canvasShooter.coords(gamePanel.shotRectangle)

    # Get the coordinates of the falling circles
    xLF1, yLF1, xLF2, yLF2 = gamePanel.canvasShooter.coords(gamePanel.largeFallingCircle1)
    xSF1, ySF1, xSF2, ySF2 = gamePanel.canvasShooter.coords(gamePanel.smallFallingCircle1)
    xLS1, yLS1, xLS2, yLS2 = gamePanel.canvasShooter.coords(gamePanel.largeFallingCircle2)
    xSS1, ySS1, xSS2, ySS2 = gamePanel.canvasShooter.coords(gamePanel.smallFallingCircle2)
    xLT1, yLT1, xLT2, yLT2 = gamePanel.canvasShooter.coords(gamePanel.largeFallingCircle3)
    xST1, yST1, xST2, yST2 = gamePanel.canvasShooter.coords(gamePanel.smallFallingCircle3)

    # Check if the shot rectangle has collided with any of the falling circles and reset the position of the circle if it has
    if ((xR1 < xLF2 and xR2 > xLF1 and yR1 < yLF2 and yR2 > yLF1)):
        resetLargeCircle1()
    elif((xR1 < xSF2 and xR2 > xSF1 and yR1 < ySF2 and yR2 > ySF1)):
        resetSmallCircle1()
    elif((xR1 < xLS2 and xR2 > xLS1 and yR1 < yLS2 and yR2 > yLS1)):
        resetLargeCircle2()
    elif((xR1 < xSS2 and xR2 > xSS1 and yR1 < ySS2 and yR2 > ySS1)):
        resetSmallCircle2()
    elif((xR1 < xLT2 and xR2 > xLT1 and yR1 < yLT2 and yR2 > yLT1)):
        resetLargeCircle3()
    elif((xR1 < xST2 and xR2 > xST1 and yR1 < yST2 and yR2 > yST1)):
        resetSmallCircle3()


def resetLargeCircle1():
    gamePanel.canvasShooter.coords(gamePanel.largeFallingCircle1, 100, 100, 150*2, 150*2)

def resetSmallCircle1():
    gamePanel.canvasShooter.coords(gamePanel.smallFallingCircle1, 400, 100, 350, 150)

def resetLargeCircle2():
    gamePanel.canvasShooter.coords(gamePanel.largeFallingCircle2, 500, 100, 350*2, 150*2)

def resetSmallCircle2():
    gamePanel.canvasShooter.coords(gamePanel.smallFallingCircle2, 800, 100, 750, 150)

def resetLargeCircle3():
    gamePanel.canvasShooter.coords(gamePanel.largeFallingCircle3, 900, 100, 550*2, 150*2)

def resetSmallCircle3():
    gamePanel.canvasShooter.coords(gamePanel.smallFallingCircle3, 1200, 100, 1150, 150)