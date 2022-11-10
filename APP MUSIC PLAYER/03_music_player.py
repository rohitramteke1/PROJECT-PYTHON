from tkinter import *
from tkinter import filedialog
import pygame
import os
from PIL import ImageTk, Image
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(True)

root = Tk()
root.title("Music Player-Rohit")
root.geometry('450x595+400+50')
root.iconbitmap('./ico/icon.ico')
root['bg'] = "#302f2f"
# FIXME Initialises the Pygame.mixer to play the music
pygame.mixer.init()

# Initially song
song = "C:/Users/ROHIT/Music/Pop Smoke - Invincible.mp3"
SongPath = os.path.dirname(song)


def add_many_song():
	global SongPath
	songs = filedialog.askopenfilenames(parent=root, initialdir="C:\\Users\\ROHIT\\Music", title="Choose Songs", filetypes=[("Music files(.mp3)", "*.mp3"), ("Audio files(.wav)", "*.wav")])

	# Loop through the songs list and replace directory and mp3
	SongPath = os.path.dirname(songs[0])
	for song in songs:
		song = song.replace(SongPath + "/", "")
		song = song.replace(".mp3", "")
		play_list_box.insert(END, song)


def add_one_song():
	global song
	global SongPath
	song = filedialog.askopenfilename(parent=root, initialdir="C:/Users/ROHIT/Music", title="Choose Songs", filetypes=[("Music files(.mp3)", "*.mp3"), ("Audio files(.wav)", "*.wav")])
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


# Create paused variable
paused = False

# NOTE: Pause Music
def pause_music(is_paused):
	global paused
	paused = is_paused
	if is_paused:
		# Unpause
		pygame.mixer.music.unpause()
		paused = False
	else:
		# Pause
		pygame.mixer.music.pause()
		paused = True


# Play the next song in Playlist
def next_song():
    try:
        # Get the current selection
        next_one = play_list_box.curselection()
        next_one = next_one[0] + 1 # because it is tuple - contain only one item
        song = play_list_box.get(next_one)

        # Recreate Directory + Song + Extension
        song = f"{SongPath}/{song}.mp3"
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

        # Clear active bar in play_list_box
        play_list_box.selection_clear(first=0, last=END)

        # Activate new song bar
        play_list_box.activate(next_one)

        # Highlight the Next song bar
        play_list_box.selection_set(first=next_one, last=None)

    # Handle the error and start the song from 1st Song
    except Exception as error:
        next_one = 0
        song = play_list_box.get(next_one)
        # Recreate Directory + Song + Extension
        song = f"{SongPath}/{song}.mp3"
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

        # Clear active bar in play_list_box
        play_list_box.selection_clear(first=0, last=END)

        # Activate Next song bar
        play_list_box.activate(next_one)

        # Highlight the Next song bar
        play_list_box.selection_set(first=next_one, last=None)

# Play Previous song in play_list_box
def previous_song():
    try:
        # Get the current selection
        previous_one = play_list_box.curselection()
        previous_one = previous_one[0] - 1 # because it is tuple - contain only one item
        song = play_list_box.get(previous_one)

        # Recreate Directory + Song + Extension
        song = f"{SongPath}/{song}.mp3"
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

        # Clear active bar in play_list_box
        play_list_box.selection_clear(first=0, last=END)

        # Activate new song bar
        play_list_box.activate(previous_one)

        # Highlight the Next song bar
        play_list_box.selection_set(first=previous_one, last=None)

    except Exception as error:
        pass
# Delete one song from Playlist       
def delete_song():
    play_list_box.delete(ANCHOR)
    pygame.mixer.music.pause()
        
# Delete all songs from Playlist
def delete_all_song():
    play_list_box.delete(0, END)
    pygame.mixer.music.pause()



# NOTE: Song list
# play_list_box = Listbox(root, bg='#302f2f', fg="#fff", height=20, width=40, selectbackground="#25a796", font=("Helvetica", 13, "bold"))
play_list_box = Listbox(root, bg='#302f2f', fg="#fff", height=20, width=40, selectbackground="#25a796", highlightthickness=0, relief="flat")
play_list_box.pack(pady=10, padx=5, fill=BOTH, expand=True)

# Operations on Button
play_btn_img = Image.open(r"music_btn\play2.png")
pause_btn_img = Image.open(r"music_btn\pause2.png")
backward_btn_img = Image.open(r"music_btn\prev2.png")
forward_btn_img = Image.open(r"music_btn\next2.png")
stop_btn_img = Image.open(r"music_btn\stop2.png")

# resize buttons
play_btn_img = play_btn_img.resize((60,60))
pause_btn_img = pause_btn_img.resize((50,50))
backward_btn_img = backward_btn_img.resize((50,50))
forward_btn_img = forward_btn_img.resize((50,50))
stop_btn_img = stop_btn_img.resize((50,50))

# Load Buttons Image's
play_btn_img = ImageTk.PhotoImage(play_btn_img)
pause_btn_img = ImageTk.PhotoImage(pause_btn_img)
backward_btn_img = ImageTk.PhotoImage(backward_btn_img)
forward_btn_img = ImageTk.PhotoImage(forward_btn_img)
stop_btn_img = ImageTk.PhotoImage(stop_btn_img)

# Create frame for Buttons
controls_btn_frame = Frame(root, bg="#302f2f")
controls_btn_frame.pack(pady=10, expand=10)

# Create buttons
play_btn = Button(controls_btn_frame, image=play_btn_img, bd=0, command=play_music, bg="#302f2f", cursor="hand2")
pause_btn = Button(controls_btn_frame, image=pause_btn_img, bd=0, command=lambda: pause_music(paused), bg="#302f2f", cursor="hand2")
backward_btn = Button(controls_btn_frame, image=backward_btn_img, bd=0, command=previous_song,  bg="#302f2f", cursor="hand2")
forward_btn = Button(controls_btn_frame, image=forward_btn_img, bd=0, command=next_song,  bg="#302f2f", cursor="hand2")
stop_btn = Button(controls_btn_frame, image=stop_btn_img, bd=0, command=stop_music, bg="#302f2f", cursor="hand2")

# BUG FIXME HACK TODO NOTE XXX
# frame_on_controls_btn_frame = Frame(controls_btn_frame, bg="red", width=100)
# frame_on_controls_btn_frame.grid()

# Pack buttons on the screen
pause_btn.grid(row=1, column=0, padx=10)
backward_btn.grid(row=1, column=1, padx=10)
play_btn.grid(row=1, column=2, padx=10)
forward_btn.grid(row=1, column=3, padx=10)
stop_btn.grid(row=1, column=4)


# Create Menu's 
main_menu = Menu(root, font=15)
root.configure(menu=main_menu)

# Add song menu
add_song_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add one song", command=add_one_song, activebackground="#04aa6d")
add_song_menu.add_command(label="Add many songs", command=add_many_song, activebackground="#04aa6d")

# add delete song menu
remove_song_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Remove Songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete a song from Playlist.", command=delete_song, activebackground="red")
remove_song_menu.add_command(label="Delete All songs from Playlist.", command=delete_all_song, activebackground="red")



root.mainloop()