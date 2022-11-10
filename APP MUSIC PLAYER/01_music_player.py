from tkinter import *
from tkinter import filedialog
import pygame
import os
from PIL import ImageTk, Image
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(True)

root = Tk()
root.title("Music Player-Rohit")
root.geometry('600x600+400+50')
root.iconbitmap('./ico/icon.ico')

# FIXME Initialises the Pygame.mixer to play the music
pygame.mixer.init()

# Initially song
song = "C:\\Users\\ROHIT\\Music\\Pop Smoke - Invincible.mp3"
SongPath = os.path.dirname(song)

def add_song():
	global song
	global SongPath
	song = filedialog.askopenfilename(parent=root, initialdir="C:\\Users\\ROHIT\\Music", title="Choose Songs", filetypes=[("Music files(.mp3)", "*.mp3"), ("Audio files(.wav)", "*.wav")])
	SongPath = os.path.dirname(song)
	song = song.replace(SongPath + "/", "")
	song = song.replace(".mp3", "")
	play_list_box.insert(END, song)
	print(song)

# NOTE: Play Selected Song
def play_music():
	try:
		# Recreate Directory + Song + Extension
		song = f"{SongPath}/{play_list_box.get(ACTIVE)}.mp3"
		print(song)
		pygame.mixer.music.load(song)
		pygame.mixer.music.play(loops=0)
	except:
		pygame.mixer.music.load("C:\\Users\\ROHIT\\Music\\Pop Smoke - Invincible.mp3")
		pygame.mixer.music.play(loops=0)
		pass

# NOTE: Stop Music
def stop_music():
	pygame.mixer.music.stop()
	play_list_box.selection_clear(ACTIVE)
	

# Song list
play_list_box = Listbox(root, bg='#302f2f', fg="#fff", height=20, width=50, selectbackground="#25a796", setgrid=True, selectborderwidth=5)
play_list_box.pack(pady=30, padx=5)

# Operations on Button
play_btn_img = Image.open(r"music_btn\play2.png")
pause_btn_img = Image.open(r"music_btn\pause2.png")
backward_btn_img = Image.open(r"music_btn\prev2.png")
forward_btn_img = Image.open(r"music_btn\next2.png")
# stop_btn_img = Image.open(r"music_btn\stop.png")

play_btn_img = play_btn_img.resize((60,60))
pause_btn_img = pause_btn_img.resize((50,50))
backward_btn_img = backward_btn_img.resize((50,50))
forward_btn_img = forward_btn_img.resize((50,50))
# stop_btn_img = stop_btn_img.resize((60,60))

# Load Buttons Image's
play_btn_img = ImageTk.PhotoImage(play_btn_img)
pause_btn_img = ImageTk.PhotoImage(pause_btn_img)
backward_btn_img = ImageTk.PhotoImage(backward_btn_img)
forward_btn_img = ImageTk.PhotoImage(forward_btn_img)
# stop_btn_img = ImageTk.PhotoImage(stop_btn_img)


# Create frame for Buttons
controls_btn_frame = Frame(root)
controls_btn_frame.pack()

# Create buttons
play_btn = Button(controls_btn_frame, image=play_btn_img, bd=0, command=play_music)
pause_btn = Button(controls_btn_frame, image=pause_btn_img, bd=0, command=stop_music)
backward_btn = Button(controls_btn_frame, image=backward_btn_img, bd=0)
forward_btn = Button(controls_btn_frame, image=forward_btn_img, bd=0)
# stop_btn = Button(controls_btn_frame, image=stop_btn_img, bd=0)

# Pack buttons on the screen
pause_btn.grid(row=0, column=0, padx=10)
backward_btn.grid(row=0, column=1, padx=10)
play_btn.grid(row=0, column=2, padx=10)
forward_btn.grid(row=0, column=3, padx=10)
# stop_btn.grid(row=0, column=4)


# Create Menu's 
main_menu = Menu(root, font=15)
root.configure(menu=main_menu)

# Add song menu
add_song_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add one song", command=add_song)




root.mainloop()