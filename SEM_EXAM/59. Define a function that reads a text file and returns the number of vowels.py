def vowel_count(text):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    count=0
    for char in text:
        if char in vowels:
            count+=1
    return count
with open("41. file.txt",'r') as input_file:
    text=input_file.read()
    
count=vowel_count(text)
print(f"Vowels: {count}")