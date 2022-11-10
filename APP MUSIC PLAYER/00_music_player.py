from tkinter import *
import pygame
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(True)

root = Tk()
root.title("Get Height and Width-Tkinter Python")
root.geometry('600x600+400+50')
# root.iconbitmap('./ico/icon.ico')

# Initialises the Pygame.mixer to play the music
pygame.mixer.init()

def play_music():
	pygame.mixer.music.load("C:\\Users\\ROHIT\\Desktop\\Python Intermediate Complete\\MODULES\\Tkinter-Codemy.com\\MUSIC\\a.mp3")
	pygame.mixer.music.play(loops=0)

play_btn = Button(root, text="Play", command=play_music)
play_btn.pack(pady=20)

stop_btn = Button(root, text="Stop", command=root.quit)
stop_btn.pack(pady=20)

root.mainloop()