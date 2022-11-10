from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk # Scrollbar
from mutagen.mp3 import MP3 # ext for length of Music
import pygame # ext
import os
import time
from PIL import ImageTk, Image # ext
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(True)

root = Tk()
root.title("Music Player-Rohit")
root.geometry('600x700+400+50')
root.iconbitmap('./ico/icon.ico')
root['bg'] = "#302f2f"
# FIXME Initialises the Pygame.mixer to play the music
pygame.mixer.init()

# Initially song
song = "C:/Users/ROHIT/Music/Pop Smoke - Invincible.mp3"
SongPath = os.path.dirname(song)
song_length = 0
song_volume = 100
# Time Duration of song
def play_time():
    try:
        # Check for double timing
        if stopped:
            return
        # Get the current time(s)
        current_time = pygame.mixer.music.get_pos() / 1000
        # HACK: to check delay between song slider and current time
        # slider_label.configure(text=f"Slider: {int(song_slider.get())} current_time: {int(current_time)}")
        # Convert current time into 24 Hr format
        converted_current_time = time.strftime('%M:%S' , time.gmtime(current_time))

        # Get Current Playing Song
        current_song = f"{SongPath}/{play_list_box.get(current_song_index)}.mp3"
        
        # Show current song name on screen
        song_name_label['text'] = play_list_box.get(current_song_index)

        # Load Song
        song_mutagen = MP3(current_song)
        # Song Length
        global song_length
        current_time += 1
        song_length = song_mutagen.info.length
        
        # Convert into Suitable Format
        current_song_length = time.strftime('%M:%S' , time.gmtime(song_length))

        # print(f"Slider: {int(song_slider.get())} Current_time: {int(current_time)}")
        # print(song_slider.get(), current_time)
        if (song_slider.get()) == int(song_length):
            status_bar_lbl.configure(text=f"{current_song_length} -/- {current_song_length}")
        
        if paused:
            pass

        elif int(song_slider.get()+1) == int(current_time): # Slider hasn't been moved
            # Update the Song Slider according to current song timer/position
            slider_position = int(song_length)
            song_slider.configure(to=slider_position, value=int(current_time))
            status_bar_lbl.configure(text=f"{converted_current_time} -/- {current_song_length}")

        else:
            slider_position = int(song_length)
            converted_current_time = time.strftime('%M:%S' , time.gmtime(song_slider.get()))

            song_slider.configure(to=slider_position, value=int(song_slider.get()))
            status_bar_lbl.configure(text=f"{converted_current_time} -/- {current_song_length}")

            # Move this thing along by one second
            next_time = int(song_slider.get()) + 1
            song_slider.configure(value=next_time)


        # Change the status bar
        # status_bar_lbl.configure(text=f"{converted_current_time} -/- {current_song_length}")

        # # Update the Song Slider according to current song timer/position
        # slider_position = int(song_length)
        # song_slider.configure(to=slider_position, value=int(current_time))

        # Update time
        status_bar_lbl.after(1000, play_time)  # 1000 'ms'
    except:
        pass

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
    # print(song)


# NOTE: Play Selected Song
def play_music():
    global current_song_index
    global stopped
    try:
        stopped = False
        # Recreate Directory + Song + Extension
        song = f"{SongPath}/{play_list_box.get(ACTIVE)}.mp3"
        current_song_index = play_list_box.curselection()
        # print(song, current_song_index)
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)
        song_slider.configure(value=0)
        status_bar_lbl.configure(text="")
    except:
        stopped = False
        pygame.mixer.music.load("C:\\Users\\ROHIT\\Music\\Pop Smoke - Invincible.mp3")
        pygame.mixer.music.play(loops=0)

    # Call the play_time() to get the time
    play_time()
    # # Update the slider according to song Length
    # slider_position = int(song_length)
    # song_slider.config(to=slider_position, value=0)


# NOTE: Stop Music
global stopped
stopped = False
def stop_music():
    # Reset Slider and Status Bar
    song_slider.configure(value=0)
    status_bar_lbl['text'] = ""
    # Stop Song from Playing
    pygame.mixer.music.stop()
    play_list_box.selection_clear(ACTIVE)
    global current_time
    current_time = 0

    # Set stopped variable to True
    global stopped
    stopped = True

# NOTE: Pause Music
global paused
paused = False
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
        # reset the status bar and slider
        song_slider.configure(value=1)
        status_bar_lbl.configure(text="")
        global current_song_index
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

        # Current Song Index
        current_song_index = play_list_box.curselection()[0]
    except:
        pass

# Play Previous song in play_list_box
def previous_song():
    global current_song_index
    try:
        # reset the status bar and slider
        song_slider.configure(value=1)
        status_bar_lbl.configure(text="")
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
    # Current Song Index
    try:
        current_song_index = play_list_box.curselection()[0]
    except:
        pass


# Delete one song from Playlist
def delete_song():
    play_list_box.delete(ANCHOR)
    # pygame.mixer.music.stop()
    stop_music()

# Delete all songs from Playlist
def delete_all_song():
    play_list_box.delete(0, END)
    # pygame.mixer.music.stop()
    stop_music()

# Create Status_Bar
def status_bar():
    frame = Frame(root)
    global status_bar_lbl
    global song_name_label
    song_name_label = Label(frame, text=f"", bg="#484943", fg='#66D9EF')
    song_name_label.pack(side=LEFT, anchor=SW)
    status_bar_lbl = Label(frame, text="Status Bar", anchor='e', fg='white', bg='#484943')
    status_bar_lbl.pack(anchor='e', fill=X)
    frame.pack(side='bottom', fill=X)

# Create Slider
def slider(event):
    try:
        song = f"{SongPath}/{play_list_box.get(current_song_index)}.mp3"
    except:
        pass

def volume(event):
    global song_volume
    pygame.mixer.music.set_volume(volume_slider.get())
    song_volume = pygame.mixer.music.get_volume()
    volume_label.configure(text=int(song_volume * 100))


    
# Create Frame For Scroll bar and For Play_list_box
master_frame = Frame(root, bg="#282923")
master_frame.pack(fill=BOTH, expand=True)

# NOTE: Create Scrollbar
song_scrollbar = Scrollbar(master_frame, orient=VERTICAL, highlightbackground='red')
song_scrollbar.pack(side=RIGHT, fill=Y)

# Create Slider
volume_frame = LabelFrame(master_frame, text="Volume", bg="#353430", fg="white")
volume_frame.pack(side=RIGHT, padx=10, pady=10)
volume_slider = ttk.Scale(volume_frame, from_ = 0, to = 1, orient=VERTICAL, value=1, command=volume, length=200)
volume_slider.pack(padx=10, pady=10)
volume_label = Label(volume_frame, text=song_volume)
volume_label.pack(padx=10, pady=10)
song_slider = ttk.Scale(root, from_ = 0, to = 100, orient=HORIZONTAL, value=0, command=slider, length=360)
song_slider.pack(pady=20)
# volume_label = Label(volume_frame, text="Volume")
# volume_label.pack()

# NOTE: Song list
# play_list_box = Listbox(root, bg='#302f2f', fg="#fff", height=20, width=40, selectbackground="#25a796", font=("Helvetica", 13, "bold"))
play_list_box = Listbox(master_frame, font=("Helvetica", 10, "bold") , yscrollcommand=song_scrollbar.set, bg='#36372f', fg="#fff", height=20, width=40, selectbackground="#25a796", highlightthickness=1, relief="flat")
play_list_box.pack(pady=20, padx=20, fill=BOTH, expand=True)
song_scrollbar.configure(command=play_list_box.yview)



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
controls_btn_frame.pack(expand=True)

# Create buttons
play_btn = Button(controls_btn_frame, image=play_btn_img, bd=0, command=play_music, bg="#302f2f", cursor="hand2")
pause_btn = Button(controls_btn_frame, image=pause_btn_img, bd=0, command=lambda: pause_music(paused), bg="#302f2f", cursor="hand2")
backward_btn = Button(controls_btn_frame, image=backward_btn_img, bd=0, command=previous_song,  bg="#302f2f", cursor="hand2")
forward_btn = Button(controls_btn_frame, image=forward_btn_img, bd=0, command=next_song,  bg="#302f2f", cursor="hand2")
stop_btn = Button(controls_btn_frame, image=stop_btn_img, bd=0, command=stop_music, bg="#302f2f", cursor="hand2")


# Pack buttons on the screen
pause_btn.grid(row=1, column=0, padx=10)
backward_btn.grid(row=1, column=1, padx=10)
play_btn.grid(row=1, column=2, padx=10)
forward_btn.grid(row=1, column=3, padx=10)
stop_btn.grid(row=1, column=4)

# Create Menu's
main_menu = Menu(root)
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


# Temporary Slider Label
# slider_label = Label(root, text="")
# slider_label.pack(pady=10)

status_bar()
root.mainloop()