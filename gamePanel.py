# import fallingCircleFunctions
from datetime import time

import fallingCircleFunctions
import main
import tkinter as tk
from tkinter import messagebox
import characterFunctions

# Create the game panel
def openGamePanel(root):
    main.isTitlePanelOpen = False
    messagebox.showinfo("Instructions", "Use the arrow keys or A and D to move left and right. Press Space to shoot. Press Tab to start the falling circles. Avoid getting hit by the circles!")
    global gamePanel
    gamePanel = tk.Frame(root, bg="#bde0fe")
    gamePanel.pack(fill="both", expand=True)

    # Characters anchor
    canvasRect = tk.Canvas(gamePanel, width=1920, height=150, bg="#03045e", highlightbackground="#ef476f", highlightthickness=5)
    canvasRect.place(relx=0.5, rely=0.85, anchor='center')

    # Character itself
    global canvasCircle
    global characterCircle
    global characterRectangle
    canvasCircle = tk.Canvas(gamePanel, width=1380, height=100, bg="#bde0fe", highlightthickness=0)
    characterCircle = canvasCircle.create_oval(9.75, 10, 92.5, 92.25, fill="#76c893", outline="white", width=2)
    characterRectangle = canvasCircle.create_rectangle(50, 0, 55, 25, fill="black", outline="#929292", width=2)
    canvasCircle.place(relx=0.5, rely=0.675, anchor='center')

    global canvasShooter
    global shotRectangle
    global largeFallingCircle1
    global smallFallingCircle1
    global largeFallingCircle2
    global smallFallingCircle2
    global largeFallingCircle3
    global smallFallingCircle3      
    canvasShooter = tk.Canvas(gamePanel, width=1380, height=525, bg="#bde0fe", highlightthickness=0)
    x1, y1, x2, y2 = canvasCircle.coords(characterRectangle)
    shotRectangle = canvasShooter.create_rectangle(x1 + 2.75, y1 + 500, x2 - 2.5, y2 + 500, fill="#ff0000", outline="#ff0000")
    largeFallingCircle1 = canvasShooter.create_oval(100, 100, 150*2, 150*2, fill='red', outline='', tags="fallingCircle")
    smallFallingCircle1 = canvasShooter.create_oval(400, 100, 350, 150, fill='blue', outline='', tags="fallingCircle")
    largeFallingCircle2 = canvasShooter.create_oval(500, 100, 350*2, 150*2, fill='green', outline='', tags="fallingCircle")
    smallFallingCircle2 = canvasShooter.create_oval(800, 100, 750, 150, fill='yellow', outline='', tags="fallingCircle")
    largeFallingCircle3 = canvasShooter.create_oval(900, 100, 550*2, 150*2, fill='purple', outline='', tags="fallingCircle")
    smallFallingCircle3 = canvasShooter.create_oval(1200, 100, 1150, 150, fill='orange', outline='', tags="fallingCircle")
    canvasShooter.place(relx=0.5, rely=0.3, anchor='center')



    # Bind the keyboard keys to the corresponding event handler
    root.bind("<Escape>", onEscapeKeyPressedEvent)  
    root.bind("<Right>", moveCharacterRight)
    root.bind("<Left>", moveCharacterLeft)
    root.bind("<d>", moveCharacterRight)
    root.bind("<a>", moveCharacterLeft)
    root.bind("<Tab>", fallingCirclesFall)
    root.unbind("<space>") # Unbind the space bar from the root window to prevent the glitch from happening when the space bar is pressed
    gamePanel.bind("<space>", fireShot)
    gamePanel.focus_set() # Set the focus to the game panel so that the space bar event handler will work when the space bar is pressed

# Event handler for the Escape key 
def onEscapeKeyPressedEvent(event):
    if main.isTitlePanelOpen:
        return
    if fallingCircleFunctions.isGameRunning:
        messagebox.showinfo("Exit Game", "You cannot exit the game while it is running. Please wait until the game is over.")
        resetTheCirclesOnExit()
        return
    leaveGameMessage = messagebox.askyesno("Leave Session", "Are you sure you want to leave?")
    
    # If the user confirms, exit the game and return to the title panel
    if leaveGameMessage:
        print("Leaving Session...")
        resetGamePanel()  
        main.openTitlePanel(root=main.main.__globals__['root'])
        main.isTitlePanelOpen = True
        resetTheCirclesOnExit()
        while main.isTitlePanelOpen == True:
            resetTheCirclesOnExit()
            time.sleep(0.1)
    else:
        pass


# Event handlers for character movement
def moveCharacterRight(event):
    characterFunctions.shiftCharacterRight(1)
    characterFunctions.startMovingRight()

def moveCharacterLeft(event):
    characterFunctions.shiftCharacterLeft(-1)
    characterFunctions.startMovingLeft()

def fireShot(event):
    characterFunctions.useShooter(-40)
    characterFunctions.startShooting()

def resetGamePanel():
    gamePanel.pack_forget()

def fallingCirclesFall(event):
        # If the game is already running, do not start it again
        if fallingCircleFunctions.isGameRunning:
            return

        fallingCircleFunctions.moveTheCirclesDown()
        fallingCircleFunctions.isGameRunning = True


# Function to reset the positions of the falling circles and stop them from moving down when the player exits the game or returns to the title panel
def resetTheCirclesOnExit(event=None):
    fallingCircleFunctions.resetLargeCircle1()
    fallingCircleFunctions.resetSmallCircle1()
    fallingCircleFunctions.resetLargeCircle2()
    fallingCircleFunctions.resetSmallCircle2()
    fallingCircleFunctions.resetLargeCircle3()
    fallingCircleFunctions.resetSmallCircle3()

    fallingCircleFunctions.largeCircle1StopMovingDown()
    fallingCircleFunctions.smallCircle1StopMovingDown()
    fallingCircleFunctions.largeCircle2StopMovingDown()
    fallingCircleFunctions.smallCircle2StopMovingDown()
    fallingCircleFunctions.largeCircle3StopMovingDown()
    fallingCircleFunctions.smallCircle3StopMovingDown()

    fallingCircleFunctions.playerIsLost()
    fallingCircleFunctions.isGameRunning = False

