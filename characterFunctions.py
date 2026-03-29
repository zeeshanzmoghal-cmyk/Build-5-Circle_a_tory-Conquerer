from time import sleep
import gamePanel
import tkinter as tk

isMovingRight = False
isMovingLeft = False
isShooting = False

# Functions to start and stop the character's movement in the right and left directions
def startMovingRight():
    global isMovingRight
    isMovingRight = True

def stopMovingRight():
    global isMovingRight
    sleep(0.5)
    isMovingRight = False

def startMovingLeft():
    global isMovingLeft
    isMovingLeft = True

def stopMovingLeft():
    global isMovingLeft
    sleep(0.5)
    isMovingLeft = False

def startShooting():
    global isShooting
    isShooting = True

def stopShooting():
    global isShooting
    isShooting = False

# Functions to move the character by a specified amount horizontally
def shiftCharacterRight(dx):
    # Check if the character is currently moving right
    if not isMovingRight:
        return

    # Move the character and the shot right by dx pixels
    gamePanel.canvasCircle.move(gamePanel.characterCircle, dx, 0)
    gamePanel.canvasCircle.move(gamePanel.characterRectangle, dx, 0)
    gamePanel.canvasShooter.move(gamePanel.shotRectangle, dx, 0)  

    # Get the coordinates of the character 
    x1, y1, x2, y2 = gamePanel.canvasCircle.coords(gamePanel.characterCircle)
    canvasWidth = gamePanel.canvasCircle.winfo_width()

    # Check if the character has moved too far right
    if x2 > canvasWidth:  
        gamePanel.canvasCircle.move(gamePanel.characterCircle, -dx, 0)  
        gamePanel.canvasCircle.move(gamePanel.characterRectangle, -dx, 0)
        gamePanel.canvasShooter.move(gamePanel.shotRectangle, -dx, 0)
        stopMovingRight()
    
    # Smoothly operate after 600 milliseconds (approximately 60 frames per second)
    gamePanel.canvasCircle.after(16, lambda: shiftCharacterRight(dx))  

def shiftCharacterLeft(dx):
    # Check if the character is currently moving left
    if not isMovingLeft:
        return
    
    # Move the character and the shot left by dx pixels
    gamePanel.canvasCircle.move(gamePanel.characterCircle, dx, 0)
    gamePanel.canvasCircle.move(gamePanel.characterRectangle, dx, 0)
    gamePanel.canvasShooter.move(gamePanel.shotRectangle, dx, 0)

    # Get the coordinates of the character 
    x1, y1, x2, y2 = gamePanel.canvasCircle.coords(gamePanel.characterCircle)

    # Check if the character has moved too far left
    if x1 < 0:  
        gamePanel.canvasCircle.move(gamePanel.characterCircle, -dx, 0)  
        gamePanel.canvasCircle.move(gamePanel.characterRectangle, -dx, 0)
        gamePanel.canvasShooter.move(gamePanel.shotRectangle, -dx, 0)
        stopMovingLeft()

    # Smoothly operate after 600 milliseconds (approximately 60 frames per second)
    gamePanel.canvasCircle.after(16, lambda: shiftCharacterLeft(dx))  

def useShooter(dy):
    print("Firing shot...")

    # Move the shot up by dy pixels
    gamePanel.canvasShooter.move(gamePanel.shotRectangle, 0, dy)

    # Get the coordinates of the shot
    x1, y1, x2, y2 = gamePanel.canvasShooter.coords(gamePanel.shotRectangle)
    x1_char, y1_char, x2_char, y2_char = gamePanel.canvasCircle.coords(gamePanel.characterRectangle)

    # Check if the shot has moved off the top of the canvas
    if y2 < 0:  
        gamePanel.canvasShooter.coords(gamePanel.shotRectangle, x1_char + 2.5, y1_char + 500, x2_char - 2.5, y2_char + 500)
        stopShooting() # x1_char + 2.5, y1_char + 525, x2_char - 2.5, y2_char + 500
    else:
        # Smoothly operate after 600 milliseconds (approximately 60 frames per second)
        gamePanel.canvasShooter.after(16, lambda: useShooter(dy))

