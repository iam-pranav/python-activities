# 🕵️‍♂️ SECRET COMPUTER CODE DECODER (For Grades 6-8) 🕵️‍♀️
# Computers don't read letters like we do; they only understand numbers.
# We use a secret master list called 'ASCII' to match every character to a number!

def find_secret_code(character):
    # Check if the user typed more than one character
    if len(character) != 1:
        return "Oops! Please enter only ONE character at a time (like 'A', 'g', or '!')"
    
    # ord() is Python's built-in magic trick to find the ASCII number
    secret_number = ord(character)
    return secret_number

# Let's try it out!
print("--- Welcome to the ASCII Secret Code Finder! ---")
user_letter = input("Enter a single letter, number, or symbol: ")

code_result = find_secret_code(user_letter)

# If it's a number, print the secret code!
if isinstance(code_result, int):
    print(f"🎉 Success! The secret computer code (ASCII) for '{user_letter}' is: {code_result}")
else:
    print(code_result)
