# Modules 
import sys
import time
import subprocess

# Install Packages from a custom function
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install("pyttsx3")
install("pyautogui")
install("speech_recognition")
install("opencv-python")

# inputs
name = input("Enter your name: ")
spotify_test = input("Do you have spotify installed? Y/N: ")
spotify_test = spotify_test.lower()
if spotify_test == "y":
    spotify_dir = input("Enter Spotify Directory: ")
else:
    spotify_dir = " "
google_word_link = input("Enter the link of blank google word document: ")
google_ppt_link = input("Enter the link of blank google slide document: ")
google_sheet_link = input("Enter the link of blank google spreadsheet document: ")
desktop_dir = input("Enter Desktop Directory: ") 

# Open/create a text file
txt = open("dirs.txt", "w")

dirs_list = [name, spotify_dir, google_word_link, google_ppt_link, google_sheet_link, desktop_dir]

for i in range(len(dirs_list)):
    txt.write(dirs_list[i])
    txt.write("\n")

txt.close()

print("\n")
finish = "User Configuration finished... Exiting the program..."

for char in finish:
    time.sleep(0.1)
    sys.stdout.write(char)

print("\n")
