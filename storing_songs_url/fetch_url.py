from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options if needed (e.g., running in headless mode)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Optional: Run in headless mode (no UI)

# Specify the path to your ChromeDriver
driver_path = 'D:\\LULLA\\Desktop\\Pora_Sona\\SEM-2\\SEC_PYTHON\\Jarvis\\storing_songs_url\\chromedriver-win64\\chromedriver.exe'  # Replace with your ChromeDriver path

# Set up the Service and WebDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)  # Use Service to specify the path

def get_youtube_url(song_name):
    try:
        # Format the search query and open YouTube
        search_query = f"{song_name} official video"
        print(f"Searching for: {search_query}")

        # Open YouTube and perform the search using Selenium
        driver.get("https://www.youtube.com/")
        
        # Wait until the search bar is present and interactable
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "search_query")))

        # Find the search bar and input the search query
        search_box = driver.find_element(By.NAME, "search_query")
        search_box.clear()  # Clear the search box before typing
        search_box.send_keys(search_query)
        search_box.submit()
        
        # Wait for search results to load and be visible
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="video-title"]')))
        
        # Get the first video URL from search results
        video_element = driver.find_element(By.XPATH, '//*[@id="video-title"]')
        youtube_url = video_element.get_attribute('href')

        print(f"Found URL: {youtube_url}")
        return youtube_url

    except Exception as e:
        print(f"Error fetching URL for {song_name}: {e}")
        return None

def create_song_dict(txt_file):
    song_dict = {}
    
    # Read the song list from the text file
    with open(txt_file, 'r') as file:
        song_names = file.readlines()
    
    # Iterate over the song names and get the YouTube URL
    for song_name in song_names:
        song_name = song_name.strip()  # Remove any extra whitespace or newline characters
        if song_name:  # Only process if song name is not empty
            youtube_url = get_youtube_url(song_name)
            
            if youtube_url:
                song_dict[song_name] = youtube_url  # Add song and its YouTube URL to the dictionary
            else:
                print(f"Could not find URL for: {song_name}")
    
    return song_dict

# Specify the path to your text file containing the song list
txt_file = 'song_titles.txt'

# Create the song dictionary
song_dict = create_song_dict(txt_file)

# Save the dictionary to a Python file
with open('songs.py', 'w') as f:
    f.write('songs_dict = ' + str(song_dict))

print("Dictionary saved to songs.py.")

# Close the browser after completing the task
driver.quit()