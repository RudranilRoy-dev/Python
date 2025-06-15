# Import necessary modules for voice recognition, text-to-speech, web scraping, browser automation, and AI
import speech_recognition as sr  # For speech recognition from microphone
import pyttsx3  # For text-to-speech conversion
import time  # For sleep/delay functions
import datetime  # To get current date and time
import os  # To execute operating system commands
import requests  # To send HTTP requests (for APIs like weather)
import webbrowser  # To open websites in the default web browser
from bs4 import BeautifulSoup  # To parse and extract data from HTML pages
from selenium import webdriver  # For browser automation (used to scrape cricket news)
from selenium.webdriver.chrome.options import Options  # To run Selenium Chrome browser in headless mode
import google.generativeai as genai  # To use Google Gemini AI
import url  # Custom module containing predefined website URLs (should have a 'links' dictionary)

# API Keys for services used
OPENWEATHER_API_KEY = "2cafee9585b2216ca921e2fd6c83b2eb"  # OpenWeatherMap API Key (replace with your own if necessary)
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"  # Replace this with your actual Gemini API Key

# Configure Gemini AI with your API key
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the speech recognizer and text-to-speech (TTS) engine
recognizer = sr.Recognizer()  # Create a Recognizer instance for speech recognition
engine = pyttsx3.init()  # Initialize the TTS engine
voices = engine.getProperty('voices')  # Get available voice profiles from TTS engine
engine.setProperty('voice', voices[0].id)  # Set the voice to the first available (usually default system voice)
engine.setProperty("rate", 130)  # Set the speech rate (words per minute)

def speak(text):
    """Speak the provided text using the TTS engine."""
    engine.say(text)  # Add the text to the TTS engine queue
    engine.runAndWait()  # Play the queued speech and wait till it's finished

def shutdown_computer():
    """Shutdown the computer with a 10-second warning."""
    speak("Shutting down your computer in 10 seconds. Save your work.")  # Warn the user
    time.sleep(10)  # Wait for 10 seconds to let user save their work
    os.system("shutdown /s /t 1")  # Execute the shutdown command (for Windows)

def tell_time():
    """Speak the current system time."""
    current_time = datetime.datetime.now().strftime("%I:%M %p")  # Format time in 12-hour format with AM/PM
    speak(f"The time is {current_time}")  # Speak the time

def tell_date():
    """Speak today's date."""
    today = datetime.datetime.now().strftime("%A, %B %d, %Y")  # Format date as weekday, month day, year
    speak(f"Today is {today}")  # Speak the date

def get_weather_openweathermap(city, api_key):
    """Fetch weather details for a city using OpenWeatherMap API."""
    try:
        # Prepare the API URL with the city and API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)  # Send GET request to OpenWeatherMap API
        data = response.json()  # Parse the returned JSON response

        # If the response is successful (HTTP 200 OK)
        if response.status_code == 200:
            temp = data["main"]["temp"]  # Extract temperature value
            weather = data["weather"][0]["description"]  # Extract weather condition description
            speak(f"It's {temp} degrees Celsius with {weather} in {city}.")  # Speak the weather info
        else:
            speak("Couldn't fetch the weather from OpenWeatherMap.")  # API returned error
    except Exception as e:
        speak(f"Error fetching weather: {e}")  # Handle exceptions (like connection errors)

def get_cricket_news():
    """Scrape top cricket news headline from ESPN Cricinfo using Selenium."""
    try:
        options = Options()  # Create options object for Chrome
        options.add_argument("--headless")  # Run browser in headless mode (without GUI)
        options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
        options.add_argument("--no-sandbox")  # Disable sandbox mode (avoids some Linux errors)
        options.add_argument("user-agent=Mozilla/5.0")  # Set browser user-agent to avoid blocking

        driver = webdriver.Chrome(options=options)  # Initialize Chrome driver with options
        driver.get("https://www.espncricinfo.com/")  # Open ESPN Cricinfo homepage
        time.sleep(3)  # Wait for page to load

        soup = BeautifulSoup(driver.page_source, "html.parser")  # Parse the loaded HTML content
        driver.quit()  # Close the browser

        headlines = soup.select("a")  # Select all anchor tags from the page
        for tag in headlines:
            text = tag.get_text(strip=True)  # Get the text content of the link
            if text and len(text.split()) > 5:  # Ignore short/irrelevant texts
                speak("Here's the top cricket news:")  # Introductory message
                speak(text)  # Speak the first valid news headline
                return  # Exit after finding the first valid headline
        speak("Couldn't find any cricket news.")  # If no suitable headline found
    except Exception as e:
        speak(f"Error getting cricket news: {e}")  # Handle and report any error

def open_website_by_keyword(website):
    """Open a website based on provided keyword from the 'url' module."""
    if website in url.links:  # Check if keyword exists in the links dictionary
        link = url.links[website]  # Get the corresponding URL
        speak(f"Opening {website}")  # Inform the user
        webbrowser.open(link)  # Open the website in default web browser
    else:
        speak("Website not found.")  # Inform if website is not mapped

def ask_gemini(prompt):
    """Send a prompt to Gemini AI and return its response."""
    try:
        model = genai.GenerativeModel('gemini-pro')  # Load Gemini model (text generation)
        response = model.generate_content(prompt)  # Generate content from Gemini AI
        return response.text.strip()  # Return the stripped text result
    except Exception as e:
        return f"Error talking to Gemini: {e}"  # Return error message if exception occurs

def processCommand(command):
    """Determine and execute the command given by the user."""
    print(f"Command: {command}")  # Print command for debugging
    command = command.lower()  # Convert command to lowercase for easy matching

    # Handle weather inquiry
    if "weather in" in command:
        city = command.split("in")[-1].strip()  # Extract city name from the command
        get_weather_openweathermap(city, OPENWEATHER_API_KEY)  # Get weather info

    # Handle cricket news inquiry
    elif "cricket news" in command or "top cricket news" in command:
        get_cricket_news()  # Fetch cricket news

    # Handle website opening
    elif command.startswith("open "):
        site = command.replace("open ", "").strip()  # Extract website keyword
        open_website_by_keyword(site)  # Open website

    # Handle shutdown command
    elif "shutdown" in command:
        shutdown_computer()  # Shut down the system

    # Handle time inquiry
    elif "what's the time" in command or "what time is it" in command:
        tell_time()  # Speak the current time

    # Handle date inquiry
    elif "what's the date" in command or "what date is it" in command:
        tell_date()  # Speak the current date

    # Handle stop command to exit the assistant
    elif "stop" in command:
        speak("Goodbye! Exiting now.")  # Farewell message
        exit()  # Exit the program

    # Handle unknown commands using Gemini AI
    else:
        speak("Let me check that for you.")  # Inform user that AI will handle this
        ai_reply = ask_gemini(command)  # Get Gemini AI response
        print(f"Gemini AI: {ai_reply}")  # Print Gemini's reply for debugging
        speak(ai_reply)  # Speak the AI-generated response

# Main execution block to keep the assistant running
if __name__ == "__main__":
    speak("Hi, I'm Jarvis, your assistant. How can I help you?")  # Greeting message

    while True:  # Continuous loop to keep listening for commands
        try:
            with sr.Microphone() as source:  # Use the system microphone as input
                print("Listening...")  # Inform user via console
                audio = recognizer.listen(source)  # Listen to the microphone
                command = recognizer.recognize_google(audio)  # Recognize speech using Google API

            if "jarvis" in command.lower():  # Check if wake word 'jarvis' was spoken
                print(f"Full command: {command}")  # Print the recognized command
                command = command.lower().replace("jarvis", "").strip()  # Remove wake word
                processCommand(command)  # Process the actual command

        except sr.UnknownValueError:
            print("Didn't catch that.")  # Handle speech recognition failure
        except sr.RequestError as e:
            print(f"Request error: {e}")  # Handle API request error
        except Exception as e:
            print(f"Error: {e}")  # Catch-all for any other exceptions
