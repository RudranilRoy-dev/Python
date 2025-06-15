# --------------------
# IMPORT LIBRARIES
# --------------------
import speech_recognition as sr  # For recognizing speech from the microphone
import pyttsx3  # For converting text to speech (TTS)
import subprocess  # To launch external applications
import pyautogui  # To simulate keyboard and mouse actions
import time  # For adding delays
import datetime  # To fetch and format the date and time
import os  # For interacting with the operating system (like opening or closing files and programs)
import requests  # For making HTTP requests (like fetching weather data)
import google.generativeai as genai  # To connect and use Google's Gemini AI model
import url  # A custom module containing website shortcut links
from selenium import webdriver  # For automating web browsers using Selenium
from selenium.webdriver.common.keys import Keys  # To simulate keyboard keys in Selenium
from selenium.webdriver.chrome.service import Service  # To set up ChromeDriver as a service
from selenium.webdriver.common.by import By  # To select elements on a webpage by ID, name, etc.
from selenium.webdriver.chrome.service import Service  # (Duplicate import, but initializes ChromeDriver service)
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume  # For controlling the system audio
from ctypes import cast, POINTER  # To cast COM interfaces (needed for audio control)
from comtypes import CLSCTX_ALL  # To define context options for COM objects

# --------------------
# INITIALIZATION
# --------------------
recognizer = sr.Recognizer()  # Creating a recognizer object for recognizing speech input
engine = pyttsx3.init()  # Initializing the text-to-speech engine
voices = engine.getProperty('voices')  # Getting available system voices
engine.setProperty('voice', voices[0].id)  # Setting the TTS engine to use the first available voice
engine.setProperty("rate", 130)  # Setting the speaking rate to 130 words per minute
browser_process = None  # Initializing a variable to store the browser process (if one is opened)

# --------------------
# BASIC SPEAK FUNCTION (SYNCHRONOUS)
# --------------------
def speak(text):
    """Speak the provided text using the TTS engine."""
    engine.say(text)  # Queue the provided text for speaking
    engine.runAndWait()  # Block while the speech is being processed and spoken

# --------------------
# WEBSITE FUNCTIONS
# --------------------
def open_website_by_keyword(keyword):
    """Open website based on provided keyword from url.links dictionary."""
    global browser_process  # Referring to the global variable
    if keyword in url.links:  # If keyword exists in our URL shortcut dictionary
        link = url.links[keyword]  # Retrieve the actual URL from the dictionary
        try:
            edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"  # Microsoft Edge path
            browser_process = subprocess.Popen([edge_path, link])  # Open Edge browser with the URL
            speak(f"Opening {keyword} in Edge")  # Inform the user
        except FileNotFoundError:  # If Edge not found
            try:
                chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # Chrome path
                browser_process = subprocess.Popen([chrome_path, link])  # Open Chrome browser with the URL
                speak(f"Opening {keyword} in Chrome")  # Inform the user
            except FileNotFoundError:  # If Chrome not found either
                speak("Neither Edge nor Chrome is installed.")  # Inform user no browser found
    else:
        speak("Website not found.")  # Inform user if keyword not in dictionary

def close_browser():
    """Close the browser if running."""
    edge_closed = os.system("taskkill /im msedge.exe /f")  # Try force-killing Edge
    chrome_closed = os.system("taskkill /im chrome.exe /f")  # Try force-killing Chrome
    
    if edge_closed == 0 or chrome_closed == 0:  # If either browser was successfully closed
        speak("Browser closed.")  # Confirm closure
    else:
        speak("No browser was open or I didn't open it.")  # Inform if nothing to close

# --------------------
# MUSIC FUNCTIONS
# --------------------
def play_song_by_keyword(keyword):
    """
    Search for a song on YouTube using Selenium and open the first video result.
    """
    chromedriver_path = r"D:\\Pora_Sona\\SEM-2\\SEC_PYTHON\\chromedriver.exe"  # Local ChromeDriver path
    service = Service(executable_path=chromedriver_path)  # Initialize ChromeDriver Service
    options = webdriver.ChromeOptions()  # Create options for Chrome
    options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
    driver = webdriver.Chrome(service=service, options=options)  # Start Chrome using Selenium

    try:
        driver.get("https://www.youtube.com")  # Open YouTube
        search_box = driver.find_element(By.NAME, "search_query")  # Locate search box
        search_box.send_keys(keyword + Keys.RETURN)  # Type search term and hit Enter
        time.sleep(2)  # Wait 2 seconds for results to load
        video = driver.find_element(By.ID, "video-title")  # Find the first video title
        video_url = video.get_attribute("href")  # Get its URL
    except Exception as e:
        speak("Error occurred while searching on YouTube.")  # Inform user on error
        print("Selenium Error:", e)  # Print error
        video_url = None  # No URL found
    finally:
        driver.quit()  # Close Selenium browser

    if video_url:  # If a video URL was found
        speak(f"Playing {keyword} for you.")  # Inform user
        browsers = {  # Define browser paths
            "Edge": r"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
            "Chrome": r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
            "Brave": r"C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe",
            "Firefox": r"C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        }
        for browser_name, browser_path in browsers.items():  # Loop through browsers
            if os.path.exists(browser_path):  # If browser exists
                try:
                    subprocess.Popen([browser_path, video_url])  # Open URL in browser
                    speak(f"Opening in {browser_name}.")  # Inform user
                    return  # Exit function after opening
                except Exception as e:
                    print(f"Failed to open in {browser_name}: {e}")  # Print error
        speak("No supported browsers found on this system.")  # Inform if no browser worked
    else:
        speak(f"Couldn't find any video like {keyword}.")  # Inform if no URL found

# --------------------
# SYSTEM CONTROL FUNCTIONS
# --------------------
def shutdown_computer():
    """Shutdown computer after warning."""
    speak("Shutting down your computer in 10 seconds. Save your work.")  # Warn user
    time.sleep(10)  # Delay 10 seconds
    os.system("shutdown /s /t 1")  # Shut down in 1 second

def pause_song():
    """Simulate pressing space to pause."""
    time.sleep(0.3)  # Small delay
    pyautogui.press('space')  # Press space (toggle pause)
    speak("Song paused.")  # Inform user

def resume_song():
    """Simulate pressing space to resume."""
    time.sleep(0.3)  # Small delay
    pyautogui.press('space')  # Press space again
    speak("Song resumed.")  # Inform user

# --------------------
# VOLUME CONTROL FUNCTIONS
# --------------------
def volume_up():
    """Increase system volume."""
    devices = AudioUtilities.GetSpeakers()  # Get speakers
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)  # Activate interface
    volume = cast(interface, POINTER(IAudioEndpointVolume))  # Cast to volume object
    current = volume.GetMasterVolumeLevelScalar()  # Get current volume
    volume.SetMasterVolumeLevelScalar(min(current + 0.1, 1.0), None)  # Increase volume
    speak("Volume increased.")  # Inform user

def volume_down():
    """Decrease system volume."""
    devices = AudioUtilities.GetSpeakers()  # Get speakers
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)  # Activate interface
    volume = cast(interface, POINTER(IAudioEndpointVolume))  # Cast to volume object
    current = volume.GetMasterVolumeLevelScalar()  # Get current volume
    volume.SetMasterVolumeLevelScalar(max(current - 0.1, 0.0), None)  # Decrease volume
    speak("Volume decreased.")  # Inform user

def mute_volume():
    """Toggle mute/unmute."""
    devices = AudioUtilities.GetSpeakers()  # Get speakers
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)  # Activate interface
    volume = cast(interface, POINTER(IAudioEndpointVolume))  # Cast to volume object
    muted = volume.GetMute()  # Get mute status
    volume.SetMute(not muted, None)  # Toggle mute
    speak("Muted." if not muted else "Unmuted.")  # Inform user

# --------------------
# TIME & DATE FUNCTIONS
# --------------------
def tell_time():
    """Tell the current time."""
    current_time = datetime.datetime.now().strftime("%I:%M %p")  # Get formatted time
    speak(f"The time is {current_time}")  # Speak time

def tell_date():
    """Tell the current date."""
    today = datetime.datetime.now().strftime("%A, %B %d, %Y")  # Get formatted date
    speak(f"Today is {today}")  # Speak date

# --------------------
# WEATHER FUNCTION
# --------------------
def get_weather(city):
    """Fetch and tell weather."""
    url_weather = f"https://wttr.in/{city}?format=3"  # URL for short weather info
    try:
        response = requests.get(url_weather)  # HTTP GET request
        if response.status_code == 200:  # If success
            speak(response.text)  # Speak weather
        else:
            speak("Couldn't fetch the weather.")  # Inform user
    except:
        speak("Error fetching weather.")  # Network or other error

# --------------------
# APPLICATION LAUNCHER
# --------------------
def open_app(app_name):
    """Open specified app."""
    apps = {  # Dictionary of app shortcuts
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "vs code": r"C:\\Users\\YourUser\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    }
    if app_name in apps:  # If app found in shortcuts
        os.startfile(apps[app_name])  # Open app
        speak(f"Opening {app_name}")  # Inform user
    else:
        speak("App not found.")  # Inform user

# --------------------
# AI RESPONSE FUNCTION
# --------------------
def ask_ai(command):
    """Send query to Gemini AI."""
    try:
        prompt = command + " Explain in simple terms for a beginner. Keep it short, accurate and easy to understand. Avoid technical language and extra formatting."  # Customize prompt
        genai.configure(api_key="AIzaSyCHjQ8emRuMIZ3qpsAdpPtCJcG1r5kSCH0")  # Configure Gemini API key
        model = genai.GenerativeModel(model_name="models/gemini-2.0-flash-lite-001")  # Select model
        response = model.generate_content(prompt)  # Get response
        result = response.text  # Extract text
        print(f"Gemini: {result}\n")  # Print result
        speak(result)  # Speak result
    except Exception as e:
        print("Error:", e)  # Print error
        speak("Something went wrong while talking to the AI.")  # Inform user

# --------------------
# CORE COMMAND HANDLER
# --------------------
def processCommand(command):
    """Process user commands and map to functions."""
    command = command.lower()  # Convert to lowercase
    words = command.split()  # Split into words
    match words:  # Pattern match commands
        case ["open", *rest]:  # If starts with "open"
            phrase = ' '.join(rest)  # Join rest words
            if phrase in ["notepad", "calculator", "vs code"]:
                open_app(phrase)  # Open app
            else:
                open_website_by_keyword(phrase)  # Open website
        case ["close", "browser"]:  # Close browser
            close_browser()
        case ["play", *rest]:  # Play music
            play_song_by_keyword(' '.join(rest))
        case ["pause"]:  # Pause music
            pause_song()
        case ["resume"]:  # Resume music
            resume_song()
        case ["shutdown"]:  # Shutdown computer
            shutdown_computer()
        case ["stop"]:  # Exit program
            speak("Goodbye! Exiting now.")
            exit()
        case ["volume", "up"]:  # Volume up
            volume_up()
        case ["volume", "down"]:  # Volume down
            volume_down()
        case ["mute", *rest] | ["unmute", *rest]:  # Mute toggle
            mute_volume()
        case ["what", "is", "the", "time"] | ["what", "time", "is", "it"]:  # Time query
            tell_time()
        case ["what", "is", "the", "date"] | ["what", "date", "is", "it"]:  # Date query
            tell_date()
        case ["weather", "in", *rest]:  # Weather query
            get_weather(' '.join(rest))
        case _:  # Any other command to AI
            ask_ai(command)

# --------------------
# MAIN LOOP — TRIGGER & LISTEN
# --------------------
if __name__ == "__main__":  # Only run if script is main
    speak("Hi, I'm Jarvis, your assistant. How can I help you?")  # Greeting
    while True:  # Infinite loop for continuous listening
        try:
            with sr.Microphone() as source:  # Open microphone
                print("Listening...")  # Console log
                audio = recognizer.listen(source)  # Listen for speech
                command = recognizer.recognize_google(audio)  # Recognize speech
            if "jarvis" in command.lower():  # If wake-word "jarvis" detected
                print(f"Full command: {command}")  # Print command
                command = command.lower().replace("jarvis", "").strip()  # Remove wake-word
                processCommand(command)  # Process cleaned command
        except sr.UnknownValueError:  # Speech not recognized
            print("Didn't catch that.")
        except sr.RequestError as e:  # API error
            print(f"Request error: {e}")
        except Exception as e:  # Other errors
            print(f"Error: {e}")