# Import necessary modules for voice recognition, TTS, web scraping, automation, and utilities
import speech_recognition as sr  # Voice recognition from microphone
import pyttsx3  # Text-to-speech engine
import time  # Used for delays and timing
import datetime  # Used to get current date and time
import os  # Used for operating system commands like shutdown
import requests  # To send HTTP requests for APIs
import webbrowser  # To open websites in a browser
from bs4 import BeautifulSoup  # To parse HTML content
from selenium import webdriver  # To automate web browser actions
from selenium.webdriver.chrome.options import Options  # To configure Chrome in headless mode
import url  # Custom module containing pre-defined website links

# Store your OpenWeatherMap API key to use in weather requests
OPENWEATHER_API_KEY = "2cafee9585b2216ca921e2fd6c83b2eb"  # Replace with your own API key if needed

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()  # Creates an instance to recognize speech from microphone
engine = pyttsx3.init()  # Initializes text-to-speech engine
voices = engine.getProperty('voices')  # Gets available voices
engine.setProperty('voice', voices[0].id)  # Sets voice to default (index 0)
engine.setProperty("rate", 130)  # Sets speech rate (speed of speech)

# Define a function to convert text to speech

def speak(text):
    """Speak the provided text using TTS engine."""
    engine.say(text)  # Queues text for speaking
    engine.runAndWait()  # Waits for the speaking to finish

# Define a function to shutdown the computer

def shutdown_computer():
    """Shutdown the computer after a brief warning."""
    speak("Shutting down your computer in 10 seconds. Save your work.")  # Warn the user
    time.sleep(10)  # Wait 10 seconds
    os.system("shutdown /s /t 1")  # Executes shutdown command (Windows)

# Define a function to tell current time

def tell_time():
    """Speak the current time."""
    current_time = datetime.datetime.now().strftime("%I:%M %p")  # Gets current time in 12-hour format
    speak(f"The time is {current_time}")  # Speaks the time

# Define a function to tell today's date

def tell_date():
    """Speak the current date."""
    today = datetime.datetime.now().strftime("%A, %B %d, %Y")  # Gets current date in readable format
    speak(f"Today is {today}")  # Speaks the date

# Define a function to fetch and speak weather using OpenWeatherMap API

def get_weather_openweathermap(city, api_key):
    """Fetches weather from OpenWeatherMap."""
    try:
        # Form the API URL with city and key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)  # Send GET request
        data = response.json()  # Parse response JSON

        # If API call was successful
        if response.status_code == 200:
            temp = data["main"]["temp"]  # Extract temperature
            weather = data["weather"][0]["description"]  # Extract weather description
            speak(f"It's {temp} degrees Celsius with {weather} in {city}.")  # Speak result
        else:
            speak("Couldn't fetch the weather from OpenWeatherMap.")  # Speak error
    except Exception as e:
        speak(f"Error fetching weather: {e}")  # Speak exception error

# Define a function to scrape and speak cricket news using Selenium

def get_cricket_news():
    """Scrape top cricket news using Selenium."""
    try:
        options = Options()  # Create options for Chrome
        options.add_argument("--headless")  # Run in headless mode (no UI)
        options.add_argument("--disable-gpu")  # Disable GPU usage
        options.add_argument("--no-sandbox")  # Prevent sandboxing issues in some environments
        options.add_argument("user-agent=Mozilla/5.0")  # Set user-agent to mimic browser

        driver = webdriver.Chrome(options=options)  # Launch Chrome browser with options
        driver.get("https://www.espncricinfo.com/")  # Open CricInfo homepage
        time.sleep(3)  # Wait for JavaScript to load content

        soup = BeautifulSoup(driver.page_source, "html.parser")  # Parse page HTML
        driver.quit()  # Close browser

        headlines = soup.select("a")  # Select all anchor tags
        for tag in headlines:
            text = tag.get_text(strip=True)  # Get cleaned text
            if text and len(text.split()) > 5:  # Skip short or irrelevant links
                speak("Here's the top cricket news:")  # Speak intro
                speak(text)  # Speak first meaningful headline
                return  # Stop after first found

        speak("Couldn't find any cricket news.")  # If no headline found
    except Exception as e:
        speak(f"Error getting cricket news: {e}")  # Speak exception error

# Define a function to open websites by keyword

def open_website_by_keyword(website):
    """Open website based on provided keyword."""
    if website in url.links:  # Check if keyword exists in links
        link = url.links[website]  # Get the URL
        speak(f"Opening {website}")  # Speak the action
        webbrowser.open(link)  # Open in browser
    else:
        speak("Website not found.")  # Speak error if not found

# Define the command processing logic

def processCommand(command):
    """Handle user command and execute appropriate function."""
    print(f"Command: {command}")  # Print the recognized command
    command = command.lower()  # Normalize to lowercase

    # If command contains weather request
    if "weather in" in command:
        city = command.split("in")[-1].strip()  # Extract city name
        get_weather_openweathermap(city, OPENWEATHER_API_KEY)  # Fetch weather

    # If command asks for cricket news
    elif "cricket news" in command or "top cricket news" in command:
        get_cricket_news()  # Fetch cricket news

    # If command starts with "open"
    elif command.startswith("open "):
        site = command.replace("open ", "").strip()  # Extract site name
        open_website_by_keyword(site)  # Open website

    # If command asks for shutdown
    elif "shutdown" in command:
        shutdown_computer()  # Shutdown PC

    # If command asks for current time
    elif "what's the time" in command or "what time is it" in command:
        tell_time()  # Speak time

    # If command asks for date
    elif "what's the date" in command or "what date is it" in command:
        tell_date()  # Speak date

    # If command is to stop the assistant
    elif "stop" in command:
        speak("Goodbye! Exiting now.")  # Speak farewell
        exit()  # Exit the program

    # If command not recognized
    else:
        speak("Command not found.")  # Speak error

# Main execution block
if __name__ == "__main__":
    speak("Hi, I'm Jarvis, your assistant. How can I help you?")  # Greet user

    while True:  # Continuous listening loop
        try:
            with sr.Microphone() as source:  # Use microphone as input source
                print("Listening...")  # Print status
                audio = recognizer.listen(source)  # Listen to audio
                command = recognizer.recognize_google(audio)  # Recognize using Google

            if "jarvis" in command.lower():  # Check for wake word
                print(f"Full command: {command}")  # Print full command
                command = command.lower().replace("jarvis", "").strip()  # Remove wake word
                processCommand(command)  # Process the command

        except sr.UnknownValueError:
            print("Didn't catch that.")  # Handle unrecognized speech

        except sr.RequestError as e:
            print(f"Request error: {e}")  # Handle API errors

        except Exception as e:
            print(f"Error: {e}")  # Handle all other errors