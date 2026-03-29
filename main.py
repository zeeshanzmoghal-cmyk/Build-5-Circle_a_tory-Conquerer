# Circle-atory Conqueror v1.0.0
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import font 
import os
from tkinter import messagebox
import gamePanel

# Global variable to hold the game panel
root = None
isTitlePanelOpen = True

# Initialize the main application window
def main():
    global root
    root = tk.Tk()
    root.title("Circle-atory Conqueror")
    root.geometry("1920x1080")
    openTitlePanel(root)

    root.mainloop()

# Function to exit the game
def exitGame():
    exitGameMessage = messagebox.askyesno("Exit Game", "Are you sure you want to exit the game?")
    # If the user confirms, exit the game
    if exitGameMessage:
        print("Exiting game...")
        sys.exit(0)
    else:
        pass

# Function to open the title panel
def openTitlePanel(root):
    # Set the background image for the title panel
    script_dir = os.path.dirname(os.path.abspath(__file__))
    bgImage = os.path.join(script_dir, "Resources", "titlePagebg-fixed.png")
    bgPhoto = tk.PhotoImage(file=bgImage, master=root) 
    print(f"Tk Version: {tk.TkVersion}")

    # Create the title panel
    titlePanel = tk.Label(root, image=bgPhoto, height=100)
    titlePanel.image = bgPhoto  # Keep a reference to the image to prevent garbage collection
    titlePanel.pack(fill="both", expand=True)

    # Styling for the buttons
    style = ttk.Style()
    adlamDisplayFont = font.Font(family="Adlam Display", size=20)
    style.configure("TButton", font=adlamDisplayFont, padding=10)

    # Function to open the game panel
    def startGame():
        titlePanel.pack_forget()  
        gamePanel.openGamePanel(root)  

    # Main Menu
    titleLabel = ttk.Label(titlePanel, text="Circle-atory Conqueror", font=("Adlam Display", 50), background='black', foreground='white')
    titleLabel.place(relx=0.5, rely=0.25, anchor='center')
    playButton = ttk.Button(titlePanel, text="Play Game", command=startGame, style="TButton")
    playButton.place(relx=0.5, rely=0.5, anchor='center')
    exitButton = ttk.Button(titlePanel, text="Exit Game", command=exitGame, style="TButton")
    exitButton.place(relx=0.5, rely=0.6, anchor='center')

# Open the window and start the game
if __name__ == "__main__":
    main()
    

