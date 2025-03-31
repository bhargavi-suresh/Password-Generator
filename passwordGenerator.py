import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    char_pool = ''
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation
    
    if not char_pool:
        raise ValueError("At least one character type must be selected")
    
    return ''.join(random.choice(char_pool) for _ in range(length))

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    password = generate_password(length)
    print(f"Generated Password: {password}")
