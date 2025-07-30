# Function to check if a string is a palindrome
def is_palindrome(text):
    # Remove spaces and convert to lowercase for uniform comparison
    clean_text = text.lower()
    
    # Check if the cleaned text is the same when reversed
    return clean_text == clean_text[::-1]

# Example usage
word = "Level"
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
