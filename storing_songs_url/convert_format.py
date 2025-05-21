# Import the dictionaries directly
from music import songs
from songs import songs_dict

# Step 1: Remove song titles from song_titles.txt if they are in songs_dict
with open('song_titles.txt', 'r', encoding='utf-8') as f:
    song_titles = [line.strip() for line in f if line.strip()]

filtered_titles = [title for title in song_titles if title not in songs_dict]

with open('song_titles.txt', 'w', encoding='utf-8') as f:
    for title in filtered_titles:
        f.write(f"{title}\n")

# Step 2: Merge and sort dictionaries
songs.update(songs_dict)
sorted_songs = dict(sorted(songs.items(), key=lambda x: x[0].lower()))

# Step 3: Overwrite music.py with the updated dictionary
with open('music.py', 'w', encoding='utf-8') as f:
    f.write('songs = {\n')
    for title, url in sorted_songs.items():
        f.write(f"    {repr(title)}: {repr(url)},\n")
    f.write('}\n')

print("✅ music.py updated successfully.")