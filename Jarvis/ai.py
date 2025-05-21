# --------------------
# IMPORT LIBRARIES
# --------------------

import speech_recognition as sr  # Library to recognize speech from microphone input
import pyttsx3  # Library for converting text to speech (TTS)
import subprocess  # Used to launch external apps (like web browsers)
import pyautogui  # Simulates keyboard/mouse actions (like pressing space)
import time  # Provides time-related functions like sleep
import datetime  # To work with current date and time
import os  # Used to interact with the OS (like opening/closing programs)
import requests  # To make HTTP requests (like checking the weather)
import google.generativeai as genai # For getting the AI result from gemini
import url  # Contains a dictionary of website shortcuts
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume  # For volume control
from ctypes import cast, POINTER  # Required for COM object casting
from comtypes import CLSCTX_ALL  # Specifies context when working with COM interfaces

# --------------------
# INITIALIZATION
# --------------------
recognizer = sr.Recognizer()  # Create recognizer object for speech recognition
engine = pyttsx3.init()  # Initialize the text-to-speech engine
voices = engine.getProperty('voices')  # Get available voices
engine.setProperty('voice', voices[0].id)  # Set voice to a specific one (here: index 0)
engine.setProperty("rate", 130)  # Set speaking rate (words per minute)
browser_process = None  # Variable to store the running browser process if opened

# --------------------
# BASIC SPEAK FUNCTION (SYNCHRONOUS)
# --------------------
def speak(text):
    """Speak the provided text using TTS engine."""
    engine.say(text)  # Queue the text to be spoken
    engine.runAndWait()  # Wait until all queued commands are finished

# --------------------
# WEBSITE FUNCTIONS
# --------------------
def open_website_by_keyword(keyword):
    """Open website based on provided keyword."""
    global browser_process  # Use the global browser_process variable
    if keyword in url.links:  # Check if the keyword exists in our custom link list
        link = url.links[keyword]  # Get the actual link from the dictionary
        try:
            # Try opening with Microsoft Edge
            edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            browser_process = subprocess.Popen([edge_path, link])  # Launch Edge with the URL
            speak(f"Opening {keyword} in Edge")
        except FileNotFoundError:
            try:
                # Fallback: try Google Chrome
                chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                browser_process = subprocess.Popen([chrome_path, link])  # Launch Chrome with the URL
                speak(f"Opening {keyword} in Chrome")
            except FileNotFoundError:
                speak("Neither Edge nor Chrome is installed.")  # Inform user if neither browser found
    else:
        speak("Website not found.")  # Handle case where keyword isn't in list

def close_browser():
    """Close browser if it's running."""
    # Try killing both Edge and Chrome processes
    edge_closed = os.system("taskkill /im msedge.exe /f")  # /f forces close
    chrome_closed = os.system("taskkill /im chrome.exe /f")
    
    # Check which one (if any) closed
    if edge_closed == 0 or chrome_closed == 0:
        speak("Browser closed.")
    else:
        speak("No browser was open or I didn't open it.")

# --------------------
# MUSIC FUNCTIONS
# --------------------
def play_song_by_keyword(keyword):

    chromedriver_path = r"D:\\Pora_Sona\\SEM-2\\SEC_PYTHON\\chromedriver.exe"
    service = Service(executable_path=chromedriver_path)

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("https://www.youtube.com")

        # Search for the query
        search_box = driver.find_element("name", "search_query")
        search_box.send_keys(keyword + Keys.RETURN)
        time.sleep(2)

        # Click on the first video link
        video = driver.find_element("id", "video-title")
        video.click()

        # Video should now start playing
        speak(f" Playing {keyword}")

    except Exception as e:
        speak("I can't find the song now, please try again later.")

# --------------------
# SYSTEM CONTROL FUNCTIONS
# --------------------
def shutdown_computer():
    """Shutdown the computer after a brief warning."""
    speak("Shutting down your computer in 10 seconds. Save your work.")  # Warning
    time.sleep(10)  # Give user a chance to cancel
    os.system("shutdown /s /t 1")  # Shutdown system in 1 second

def pause_song():
    """Pause currently playing song."""
    time.sleep(0.3)  # Short delay to make it responsive
    pyautogui.press('space')  # Simulate spacebar (pauses YouTube/video)
    speak("Song paused.")

def resume_song():
    """Resume currently paused song."""
    time.sleep(0.3)
    pyautogui.press('space')  # Same as pause — space toggles play/pause
    speak("Song resumed.")

# --------------------
# VOLUME CONTROL FUNCTIONS
# --------------------
def volume_up():
    """Increase system volume."""
    devices = AudioUtilities.GetSpeakers()  # Get speaker device
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)  # Activate audio endpoint
    volume = cast(interface, POINTER(IAudioEndpointVolume))  # Cast to volume control interface
    current = volume.GetMasterVolumeLevelScalar()  # Get current volume (0.0 - 1.0)
    volume.SetMasterVolumeLevelScalar(min(current + 0.1, 1.0), None)  # Increase by 10%, max 100%
    speak("Volume increased.")

def volume_down():
    """Decrease system volume."""
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current = volume.GetMasterVolumeLevelScalar()
    volume.SetMasterVolumeLevelScalar(max(current - 0.1, 0.0), None)  # Decrease volume, min 0%
    speak("Volume decreased.")

def mute_volume():
    """Mute or unmute system volume."""
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    muted = volume.GetMute()  # Check if currently muted
    volume.SetMute(not muted, None)  # Toggle mute
    speak("Muted." if not muted else "Unmuted.")  # Respond based on action taken

# --------------------
# TIME & DATE FUNCTIONS
# --------------------
def tell_time():
    """Speak the current time."""
    current_time = datetime.datetime.now().strftime("%I:%M %p")  # Format time in AM/PM
    speak(f"The time is {current_time}")

def tell_date():
    """Speak the current date."""
    today = datetime.datetime.now().strftime("%A, %B %d, %Y")  # Full date like "Sunday, April 20, 2025"
    speak(f"Today is {today}")

# --------------------
# WEATHER FUNCTION
# --------------------
def get_weather(city):
    """Get the weather for a specific city."""
    url_weather = f"https://wttr.in/{city}?format=3"  # Format: short weather summary
    try:
        response = requests.get(url_weather)  # Send HTTP GET request
        if response.status_code == 200:  # Success
            speak(response.text)  # Speak the weather info
        else:
            speak("Couldn't fetch the weather.")
    except:
        speak("Error fetching weather.")  # Catch network/API issues

# --------------------
# APPLICATION LAUNCHER
# --------------------
def open_app(app_name):
    """Open a specific app based on its name."""
    apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "vs code": r"C:\\Users\\YourUser\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    }
    if app_name in apps:
        os.startfile(apps[app_name])  # Launch the app using system path
        speak(f"Opening {app_name}")
    else:
        speak("App not found.")  # Inform user if shortcut not listed

# --------------------
# AI RESPONSE FUNCTION
# --------------------
def ask_ai(command):                # 🧠 Define a function that sends a prompt to Gemini API
    try:
        prompt = command + " Explain in simple terms for a beginner. Keep it short, accurate and easy to understand. Avoid technical language and extra formatting."
        genai.configure(api_key="AIzaSyCHjQ8emRuMIZ3qpsAdpPtCJcG1r5kSCH0")
        model = genai.GenerativeModel(model_name="models/gemini-2.0-flash-lite-001")
        response = model.generate_content(prompt)
        result=response.text
        print(f"Gemini: {result}\n")
        speak(result)
    except Exception as e:
        print("Error:", e)                          # 🐞 Print the actual error for debugging
        speak("Something went wrong while talking to the AI.")  # ❗ Generic spoken error message

# --------------------
# CORE COMMAND HANDLER
# --------------------
def processCommand(command):
    """Handle user command and execute appropriate function."""
    command = command.lower()  # Normalize command to lowercase
    words = command.split()  # Split command into list of words

    # Pattern matching using match-case (Python 3.10+)
    match words:
        case ["open", *rest]:
            phrase = ' '.join(rest)  # Join rest of words
            if phrase in ["notepad", "calculator", "vs code"]:
                open_app(phrase)
            else:
                open_website_by_keyword(phrase)

        case ["close", "browser"]:
            close_browser()

        case ["play", *rest]:
            play_song_by_keyword(' '.join(rest))  # Play music based on name

        case ["pause"]:
            pause_song()

        case ["resume"]:
            resume_song()

        case ["shutdown"]:
            shutdown_computer()

        case ["stop"]:
            speak("Goodbye! Exiting now.")  # Graceful shutdown
            exit()

        case ["volume", "up"]:
            volume_up()

        case ["volume", "down"]:
            volume_down()

        case ["mute", *rest] | ["unmute", *rest]:
            mute_volume()

        case ["what","is", "the", "time"] | ["what", "time", "is", "it"]:
            tell_time()

        case ["what","is", "the", "date"] | ["what", "date", "is", "it"]:
            tell_date()

        case ["weather", "in", *rest]:
            get_weather(' '.join(rest))

        case _:
            ask_ai(command)  # If command doesn't match any predefined case, ask the AI

# --------------------
# MAIN LOOP — TRIGGER & LISTEN
# --------------------
if __name__ == "__main__":
    speak("Hi, I'm Jarvis, your assistant. How can I help you?")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio)

            if "jarvis" in command.lower():
                print(f"Full command: {command}")
                command = command.lower().replace("jarvis", "").strip()
                processCommand(command)

        except sr.UnknownValueError:
            print("Didn't catch that.")

        except sr.RequestError as e:
            print(f"Request error: {e}")

        except Exception as e:
            print(f"Error: {e}")