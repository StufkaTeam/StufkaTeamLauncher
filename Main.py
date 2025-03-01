import tkinter as tk
from tkinter import PhotoImage
import subprocess
import os
from tkinter import font as tkFont
import webbrowser
from PIL import Image, ImageTk

fontsize = 20

def start_game_polish():
    try:
        print("Polish")
        game_path = os.path.join('GameFiles', 'Polish', 'MH2.exe')
        subprocess.Popen(game_path, creationflags=subprocess.CREATE_NO_WINDOW)
    except Exception as e:
        print(f"An error occurred: {e}")

def start_game_english():
    try:
        print("English")
        game_path = os.path.join('GameFiles', 'English', 'MH2.exe')
        subprocess.Popen(game_path, creationflags=subprocess.CREATE_NO_WINDOW)
    except Exception as e:
        print(f"An error occurred: {e}")

def check_changelog(language):
    if language == "Polish":
        changelog_path = os.path.join(os.path.dirname(__file__), "Launcher", "Html", "ChangelogPol.html")
    elif language == "English":
        changelog_path = os.path.join(os.path.dirname(__file__), "Launcher", "Html", "ChangelogEng.html")
    webbrowser.open(changelog_path)

def show_play_buttons(language):
    button1.place_forget()
    button2.place_forget()
    if language == "Polish":
        play_command = start_game_polish
        changelog_command = lambda: check_changelog("Polish")
        play_text = "Graj"
        changelog_text = "Changelog"
    else:
        play_command = start_game_english
        changelog_command = lambda: check_changelog("English")
        play_text = "Play"
        changelog_text = "Changelog"
    
    play_button = tk.Button(root, text=play_text, command=play_command, font=button_font, width=150, height=50, image=button_bg_image, compound="center", bg='black', highlightbackground='black', activebackground='red')
    play_button.place(relx=0.4, rely=0.5, anchor='center')
    changelog_button = tk.Button(root, text=changelog_text, command=changelog_command, font=button_font, width=150, height=50, image=button_bg_image, compound="center", bg='black', highlightbackground='black', activebackground='red')
    changelog_button.place(relx=0.6, rely=0.5, anchor='center')

    # Show button3, button4, button5, button6, button7, and button8
    update_button_positions()

    # Bind hover events to new buttons
    play_button.bind("<Enter>", on_enter)
    play_button.bind("<Leave>", on_leave)
    changelog_button.bind("<Enter>", on_enter)
    changelog_button.bind("<Leave>", on_leave)

def on_enter(e):
    e.widget['background'] = 'red'
    e.widget['foreground'] = 'black'

def on_leave(e):
    e.widget['background'] = 'black'
    e.widget['foreground'] = 'black'

def update_button_positions():
    window_width = root.winfo_width()
    window_height = root.winfo_height()

    button3.place(x=window_width - button3.winfo_width() - 20, y=window_height - button3.winfo_height() - 20)
    button4.place(x=window_width - button4.winfo_width() - button3.winfo_width() - 40, y=window_height - button4.winfo_height() - 20)
    button8.place(x=window_width - button8.winfo_width() - button4.winfo_width() - button3.winfo_width() - 60, y=window_height - button8.winfo_height() - 20)
    button5.place(x=20, y=window_height - button5.winfo_height() - 20)
    button6.place(x=button5.winfo_width() + 40, y=window_height - button6.winfo_height() - 20)
    button7.place(x=button5.winfo_width() + button6.winfo_width() + 60, y=window_height - button7.winfo_height() - 20)

# Set up the main window
root = tk.Tk()
root.title("Stufka Team Launcher")
root.geometry("1024x768")
root.minsize(1024, 768)
root.maxsize(1920, 1080)
root.configure(background='black')

# Load the background image
background_image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "Launcher", "Img", "Background.png"))
background_image = PhotoImage(file=background_image_path)

# Create a label to hold the background image
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Load the custom font
custom_font = tkFont.Font(family="Ubuntu", size=(fontsize), weight="bold")

# Load the button background image
button_bg_image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "Launcher", "Img", "ButtonBackground.png"))
button_bg_image = PhotoImage(file=button_bg_image_path)

# Load and resize the new image for button3
button3_image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "Launcher", "Img", "StufkaTeam1000x1000.png"))
button3_image = Image.open(button3_image_path)
button3_image = button3_image.resize((button3_image.width // 12, button3_image.height // 12), Image.LANCZOS)
button3_image = ImageTk.PhotoImage(button3_image)

# Load and resize the new image for button4
button4_image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "Launcher", "Img", "gamejolt.png"))
button4_image = Image.open(button4_image_path)
button4_image = button4_image.resize((button4_image.width // 12, button4_image.height // 12), Image.LANCZOS)
button4_image = ImageTk.PhotoImage(button4_image)

# Load and resize the new image for button5 (Twitter)
button5_image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "Launcher", "Img", "twitter.png"))
button5_image = Image.open(button5_image_path)
button5_image = button5_image.resize((button5_image.width // 12, button5_image.height // 12), Image.LANCZOS)
button5_image = ImageTk.PhotoImage(button5_image)

# Load and resize the new image for button6 (Discord)
button6_image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "Launcher", "Img", "discord.png"))
button6_image = Image.open(button6_image_path)
button6_image = button6_image.resize((button6_image.width // 12, button6_image.height // 12), Image.LANCZOS)
button6_image = ImageTk.PhotoImage(button6_image)

# Load and resize the new image for button7 (YouTube)
button7_image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "Launcher", "Img", "youtube.png"))
button7_image = Image.open(button7_image_path)
button7_image = button7_image.resize((button7_image.width // 12, button7_image.height // 12), Image.LANCZOS)
button7_image = ImageTk.PhotoImage(button7_image)

# Load and resize the new image for button8 (Bug Reporting)
button8_image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "Launcher", "Img", "bug.png"))
button8_image = Image.open(button8_image_path)
button8_image = button8_image.resize((button8_image.width // 12, button8_image.height // 12), Image.LANCZOS)
button8_image = ImageTk.PhotoImage(button8_image)

# Create and place the language selection buttons
button_font = tkFont.Font(family="Ubuntu", size=(fontsize))
button1 = tk.Button(root, text="Polski", command=lambda: show_play_buttons("Polish"), font=tkFont.Font(family="Ubuntu" , size=(fontsize),), width=150, height=50, image=button_bg_image, compound="center", bg='black', highlightbackground='black', activebackground='red')
button1.place(relx=0.4, rely=0.5, anchor='center')
button2 = tk.Button(root, text="English", command=lambda: show_play_buttons("English"), font=tkFont.Font(family="Ubuntu" , size=(fontsize),), width=150, height=50, image=button_bg_image, compound="center", bg='black', highlightbackground='black', activebackground='red')
button2.place(relx=0.6, rely=0.5, anchor='center')

# Create button3, button4, button5, button6, button7, and button8 but do not place them yet
button3 = tk.Button(root, image=button3_image, command=lambda: webbrowser.open("https://sites.google.com/view/stufkateam"), bg='black', highlightbackground='black', activebackground='red', borderwidth=0)
button4 = tk.Button(root, image=button4_image, command=lambda: webbrowser.open("https://gamejolt.com/@Stufka_Team"), bg='black', highlightbackground='black', activebackground='red', borderwidth=0)
button5 = tk.Button(root, image=button5_image, command=lambda: webbrowser.open("https://x.com/StufkaTeam"), bg='black', highlightbackground='black', activebackground='red', borderwidth=0)
button6 = tk.Button(root, image=button6_image, command=lambda: webbrowser.open("https://discord.com/invite/5sepT5feDR"), bg='black', highlightbackground='black', activebackground='red', borderwidth=0)
button7 = tk.Button(root, image=button7_image, command=lambda: webbrowser.open("https://www.youtube.com/@stufkateam"), bg='black', highlightbackground='black', activebackground='red', borderwidth=0)
button8 = tk.Button(root, image=button8_image, command=lambda: webbrowser.open("https://forms.gle/1Mx2TfG5pBMWiDbh8"), bg='black', highlightbackground='black', activebackground='red', borderwidth=0)

# Bind hover events to buttons
button1.bind("<Enter>", on_enter)
button1.bind("<Leave>", on_leave)
button2.bind("<Enter>", on_enter)
button2.bind("<Leave>", on_leave)
button3.bind("<Enter>", on_enter)
button3.bind("<Leave>", on_leave)
button4.bind("<Enter>", on_enter)
button4.bind("<Leave>", on_leave)
button5.bind("<Enter>", on_enter)
button5.bind("<Leave>", on_leave)
button6.bind("<Enter>", on_enter)
button6.bind("<Leave>", on_leave)
button7.bind("<Enter>", on_enter)
button7.bind("<Leave>", on_leave)
button8.bind("<Enter>", on_enter)
button8.bind("<Leave>", on_leave)

# Bind the configure event to update button positions when the window is resized
root.bind("<Configure>", lambda event: update_button_positions())

# Run the application
root.mainloop()