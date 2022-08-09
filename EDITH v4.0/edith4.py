'''Copyrighted By Param'''

# More Features coming soon with a cool user interface design

# Importing functions
import pyttsx3
import webbrowser
import time
import datetime
import pyautogui
import os
import speech_recognition as sr
import sys
import cv2

# Functions
def speak(audio):
    '''Call this function for text to speech'''
    engine.say(audio)
    engine.runAndWait()

def listen():
    '''Takes an audio input'''
    r = sr.Recognizer()
    with sr.Microphone() as audio_source:
        r.adjust_for_ambient_noise(audio_source)
        time.sleep(1)
        speak("Please Speak now...")
        listened_str_in = r.listen(audio_source)
    try:
        listened_str = r.recognize_google(listened_str_in)
        return str(listened_str.lower())
    except sr.UnknownValueError:
        return("Speak Again")
    except sr.RequestError as e:
        return(f"Could not fetch results from Google {e}\n Try Again\n")
    

def translate_time(hour, minute):
    hours = ['','ONE ', 'TWO ', 'THREE ', 'FOUR ', 'FIVE ', 'SIX ', 'SEVEN ', 'EIGHT ', 'NINE ', 'TEN ', 'ELEVEN ', 'TWELVE ']
    
    minutes = [' ', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'ELEVEN', 'TWELVE', 'THIRTEEN', 'FOURTEEN',
     'FIFTEEN', 'SIXTEEN', 'SEVENTEEN', 'EIGHTEEN', 'NINETEEN', 'TWENTY', 'TWENTY ONE', 'TWENTY TWO', 'TWENTY THREE',
     'TWENTY FOUR', 'TWENTY FIVE', 'TWENTY SIX', 'TWENTY SEVEN', 'TWENTY EIGHT', 'TWENTY NINE', 'THIRTY', 'THIRTY ONE',
     'THIRTY TWO', 'THIRTY THREE', 'THIRTY FOUR', 'THIRTY FIVE', 'THIRTY SIX', 'THIRTY SEVEN', 'THIRTY EIGHT', 'THIRTY NINE', 'FOURTY',
     'FOURTY ONE', 'FOURTY TWO', 'FOURTY THREE', 'FOURTY FOUR', 'FOURTY FIVE', 'FOURTY SIX', 'FOURTY SEVEN', 'FOURTY EIGHT', 'FOURTY NINE', 'FIFTY',
     'FIFTY ONE', 'FIFTY TWO', 'FIFTY THREE', 'FIFTY FOUR', 'FIFTY FIVE', 'FIFTY SIX', 'FIFTY SEVEN', 'FIFTY EIGHT', 'FIFTY NINE']

    hour = hours[hour]
    minute = minutes[minute]

    c_time = hour + minute 
    return c_time 

def open_google():
    '''Opens google.com'''
    webbrowser.open("www.google.com")

def search_web(string):
    '''Pastes the string on googles.com'''
    webbrowser.open("www.google.com")
    time.sleep(25)
    pyautogui.write(string)
    pyautogui.press('enter')

def open_youtube():
    '''Opens youtube.com'''
    webbrowser.open("www.youtube.com")

def get_weather():
    '''Opens accuweather.com'''
    webbrowser.open("https://www.accuweather.com/en/in/ahmedabad/202438/weather-forecast/202438")

def open_whatsapp():
    '''Opens WhatsApp Web'''
    webbrowser.open("https://web.whatsapp.com")

def open_maps():
    webbrowser.open("https://www.google.com/maps")

def dir_parse_funct(string):
    '''Parses string and removes "\n" character'''
    string = string.strip('\n')
    return str(string) 

# Pre Defining Module functions

# @pyttsx3
engine = pyttsx3.init('sapi5')
engine.setProperty("rate", 150)
engine.setProperty("volume", 1)

# @time
t = time.localtime()
current_time = time.strftime("%I %M %p", t)
current_time = current_time.upper()
current_time_speaky = current_time[0] + current_time[1] + current_time[2] + current_time[3] + current_time[4] + current_time[5] + " " + current_time[6] + " " + current_time[7]

# @datetime
current_date = datetime.datetime.today()
current_date = current_date.strftime("%A %dth %B %Y")

# @speech_recognition
r = sr.Recognizer()

# @directories
txt = open("dirs.txt", 'r')

name = txt.readlines(1)
name = str(name[0])
name = dir_parse_funct(name)

spotify_dir = txt.readlines(2)
spotify_dir = str(spotify_dir[0])
spotify = dir_parse_funct(spotify_dir)

word_link = txt.readlines(3)
word_link = str(word_link[0])
google_word = dir_parse_funct(word_link)

ppt_link = txt.readlines(4)
ppt_link = str(ppt_link[0])
google_ppt = dir_parse_funct(ppt_link)

spread_link = txt.readlines(5)
spread_link = str(spread_link[0])
google_spreadsheet = dir_parse_funct(spread_link)

desktop_dir = txt.readlines(6)
desktop_dir = desktop_dir[0]
desktop = dir_parse_funct(desktop_dir)

txt.close()


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Infinite working logic
print(f"Hey {name}! How are you?")
print(current_date)
print(current_time, "\n")
speak(f"Hey {name}! How are you? Today's date is {current_date} and its currently {current_time_speaky}")

type_of_input = input("Do you want to give a text input or speech input: ")
type_of_input = type_of_input.lower()

while True:

    print("EDITH: How may I help you?")
    speak("How may I help you?")
    
    if type_of_input == "text":
        user_input = input("") #text input selection
    elif type_of_input == "speech":
        user_input = listen() #audio input selection
    else:
        print("Enter a valid input (text/speech)")
    print(f"YOU: {user_input}")

    if user_input == "open google":
        print("EDITH: Opening Google...")
        speak("Opening Google")
        open_google()
        speak("opened Google successfully")
        print("\n")

    if user_input == "do a web search":
        print("EDITH: What should I search on web")
        speak("What should I search on web?")
        if type_of_input == "text":
            str_input = input("")
        elif type_of_input == "speech":
            str_input = listen()
        print(f"EDITH: Searching {str_input} on web...")
        speak(f"Searching {str_input} on web")
        search_web(str_input)
        print("\n")

    if user_input == "open spotify":
        if spotify == " ":
            print("Spotify isn't installed in your computer...")
            speak("Sspottifive  isn't installed in your computer")
            pass
        
        else: 
            print("EDITH: Opening Spotify... \n")
            speak("Opening Sspotteefive ")
            os.system(fr"{spotify}")
            speak("opened  Sspottifive successfully")
    
    if (user_input == "open google word") or (user_input == "open google docs"):
        print("EDITH: Opening Google Docs Word Document")
        speak("Opening Google Word Document")
        webbrowser.open(f"{google_word}")
        speak("Opened docs successfully")
        print("\n")
    
    if (user_input == "open google slides") or (user_input == "open google ppt"):
        print("EDITH: Opening Google Docs Slide Document")
        speak("Opening Google Word Document")
        webbrowser.open(f"{google_ppt}")
        speak("Opened slides successfully")
        print("\n")
    
    if (user_input == "open google sheets") or (user_input == "open google spreadsheet"):
        print("EDITH: Opening Google Docs Spreadsheet Document")
        speak("Opening Google Word Document")
        webbrowser.open(f"{google_spreadsheet}")
        speak("Opened spreadsheet successfully")
        print("\n")

    if user_input == "open a website":
        print("EDITH: Enter the website")
        speak("Enter the website")
        web = input("")
        web = str(web)
        web_1 = web[0] + web[1] + web[2] + web[3]
        web_2 = web[0] + web[1] + web[2] + web[3] + web[4]
        if web_1 == "www.":
            pass
        if web_2 == "https":
            pass
        else:
            web = "https://"+web
        
        print(f"EDITH: Opening {web} on Chrome")
        speak(f"Opening {web} on Chrome")
        webbrowser.open(web)
        print("\n")

    if user_input == "create a folder":
        print("EDITH: Enter folder name")
        speak("Enter folder name")
        if type_of_input == "text":
            foldr_name = input("")
        elif type_of_input == "speech":
            foldr_name = listen()
        parent_dir = f"{desktop}"
        path = os.path.join(f"{parent_dir}", foldr_name)
        os.mkdir(path)
        print(f"EDITH: The folder {foldr_name} has been created in {parent_dir} or Desktop...")
        speak(f"Created {foldr_name} folder on Desktop successfully")
        print("\n")
    
    if (user_input == "open a text file") or (user_input == "open a txt file"):
        current_dir = os.getcwd()
        os.chdir(fr"{desktop}")
        print("EDITH: Enter the name of file")
        speak("Enter the name of file")
        if type_of_input == "text":
            x112_name = input("")
        elif type_of_input == "speech":
            x112_name = listen()
        print(f"YOU: {x112_name}")
        x112_name = x112_name + ".txt"
        x112 = open(x112_name, "w")
        print("EDITH: Opening a text file...")
        speak("Opening a text file")
        os.startfile(x112_name)
        speak("Opened text file successfully")
        x112.close()
        os.chdir(current_dir)
        print("\n")
    
    if user_input == "open youtube":
        print("EDITH: Opening YouTube...")
        speak("Opening Youtube on Chrome")
        open_youtube()
        speak("Opened YouTube Successfully")
        print("\n")
    
    if user_input == "open calculator":
        print("EDITH: Opening calculator...")
        speak("Opening calculator")
        speak("Opened calculator successfully")
        os.system(r'C:\Windows\system32\calc.exe')
        print("\n")
    
    if user_input == "take a screenshot":
        print("EDITH: What should I name screenshot?")
        speak("What should I name screenshot")
        if type_of_input == "text":
            x235_name = input("")
        elif type_of_input == "speech":
            x235_name = listen()
        print(f"YOU: {x235_name}")
        print("EDITH: Taking Screenshot")
        speak("Taking screenshot")
        speak("5")
        time.sleep(1)
        speak("4")
        time.sleep(1)
        speak("3")
        time.sleep(1)
        speak("2")
        time.sleep(1)
        speak("1")
        time.sleep(1)
        print("EDITH: Screenshot taken successfully")
        speak("Screenshot taken successfully")
        x235 = pyautogui.screenshot()
        x235.save(fr'{desktop}\{x235_name}.png')
        print("\n")
    
    if (user_input == "weather forecast") or (user_input == "what is the weather today"):
        print("EDITH: Opening www.accuweather.com")
        speak("Opening W W W dot A Q weather dot com")
        get_weather()        
        print("\n")

    if (user_input == "open gmail") or (user_input == "open email"):
        print("EDITH: Opening gmail")
        speak("Opening mail")
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        speak("Opened e-mail successfully")
        print("\n")

    if (user_input == "open whatsapp") or (user_input == "open what's up"):
        print("EDITH: Opening WhatsApp Web")
        speak("Opening WhatsApp Web")
        open_whatsapp()
        speak("Opened WhatsApp Web successfully")
        print("\n")

    if user_input == "open maps":
        print("EDITH: Opening maps")
        speak("Opening maps")
        open_maps()
        speak("Opened maps successfully")

    if user_input == "command assistant tasks" :
        print("I can open Google or do a web search or open a website")
        speak("I can open Google or do a web search or open a website")
        print("I can open spotify, calculator, youtube,  create a text file and folder")
        speak("I can open sspotteefive, calculator, youtube,  create a text file and folder")
        print("I can also open google docs, ppt and spreadsheet")
        speak("I can also open google docs, ppt and spreadsheet")
        print("I can take a screenshot or play some music for you ;)\n")
        speak("I can take a screenshot or play some music for you")
   
    if user_input == "who are you":
        print("I am the EDITH\n")
        speak("I am the EDITH")
    
    if user_input == "commands":
        print("open google\ndo a web search\nopen spotify\nopen google word\nopen google slides\nopen google sheets\nopen a website\ncreate a folder\nopen a text file\nplay a song\nopen youtube\nopen calculator\ntake a screenshot\nweather forecast\nopen gmail\n")
        speak("Here are the tasks I can perform")

    if user_input == "exit":
        exit_line = "Exiting EDITH AI Assistant program..."
        for char in exit_line:
            time.sleep(0.1)
            sys.stdout.write(char)
        print("\n")
        speak("Exiting EDITH A I Assistant program...")
        speak("Exited successfully")
        break

    if user_input == "what is current time":
        print(current_time,"\n")
        speak(current_time_speaky)

    if user_input == "what is current date":
        print(current_date,"\n")
        speak(current_date)

    if (user_input == "take a photo") or (user_input == "capture an image") or (user_input == "open camera"):
        
        print("EDITH: Enter the name of image: ")
        speak("Enter the name of image")
        
        if type_of_input == "text":
            x_img_name = input("")
        elif type_of_input == "speech":
            x_img_name = listen()
        
        print("EDITH: Opening Camera")
        speak("Opening Camera")
        speak("Enter 'Q' to Quit and 'C' to capture image")
        print("EDITH: Enter 'Q' to Quit and 'C' to capture image")
        video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        image_counter = 0

        while True:
            check, frame = video.read()
            gray_f = cv2.flip(frame, 1)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            gray_flip = cv2.flip(frame, 1)
            cv2.imshow('Camera', gray_flip)
            key = cv2.waitKey(1)

            if key == ord('q'):
                break
            if key == ord('c'):
                cv2.imwrite(fr"{desktop}\{x_img_name}.jpg", frame)
                
        # The break statement will be directed here('q')
        video.release()
        cv2.destroyAllWindows()

    if user_input == "print what i say":
        print("EDITH: For how much cycles I need to print...?")
        speak("For how much cycles I need to print")
        audio_cycles = int(listen())
        print(audio_cycles)
        for i in range(audio_cycles):
            speak("Listening...")
            audio1 = listen()
            print(audio1, "\n")

# The break statement will be directed here after (exit command for edith)