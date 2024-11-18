import re

# List of top 50 most commonly used passwords
common_passwords = [
    "123456", "password", "123456789", "12345678", "12345", "1234567", "1234567890",
    "qwerty", "abc123", "password1", "111111", "123123", "admin", "letmein", "welcome",
    "monkey", "1234", "1q2w3e4r", "sunshine", "superman", "iloveyou", "654321",
    "qwerty123", "121212", "dragon", "666666", "trustno1", "112233", "charlie",
    "hunter", "7777777", "password123", "baseball", "555555", "football", "qwertyuiop",
    "jordan23", "shadow", "michael", "biteme", "lovely", "princess", "ashley",
    "pepper", "987654321", "hello", "freedom", "whatever", "qazwsx"
]

def check_password_strength(password):
    # Check for common passwords (case-insensitive)
    if password.lower() in (common_password.lower() for common_password in common_passwords):
        return "Common Password - Very Weak. Tip: Avoid using commonly used passwords like 'password123'. Use a mix of uppercase, lowercase, numbers, and special characters.", False

    # Define criteria for password strength
    length_criteria = len(password) >= 8
    digit_criteria = re.search(r"\d", password) is not None
    uppercase_criteria = re.search(r"[A-Z]", password) is not None
    lowercase_criteria = re.search(r"[a-z]", password) is not None
    special_char_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    # Evaluate password strength
    score = sum([length_criteria, digit_criteria, uppercase_criteria, lowercase_criteria, special_char_criteria])
    strength = {
        5: "Very Strong",
        4: "Strong",
        3: "Moderate",
        2: "Weak",
        1: "Very Weak",
        0: "Invalid"
    }

    return strength[score], True

print("Function defined successfully!")

# Keep looping until a valid password is entered
while True:
    password = input("Enter your password: ")
    strength, is_valid = check_password_strength(password)
    print(f"Password entered: {password}")
    print(f"Your password strength is: {strength}")
    
    # If the password is valid (not a common password), break the loop
    if is_valid:
        break
    else:
        print("Please try again with a stronger password.")