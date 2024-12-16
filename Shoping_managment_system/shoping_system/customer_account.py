import re

def is_valid_email(email):
    """Check if the email format is valid."""
    pattern = r'^[\w.-]+@[\w.-]+\.\w{2,}$'
    return re.match(pattern, email) is not None

def is_valid_phone(phone):
    """Check if the phone number is valid (10-15 digits)."""
    return phone.isdigit() and 10 <= len(phone) <= 15

def is_strong_password(password):
    """Check if the password is strong (minimum 8 characters, includes uppercase, lowercase, number, and special character)."""
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return re.match(pattern, password) is not None

def create_customer_account():
    """Function to create a customer account with input validation."""
    print("\n--- Create Customer Account ---")
    
    # Input: Customer Name
    while True:
        name = input("Enter your full name: ").strip()
        if name:
            break
        else:
            print("Name cannot be empty. Please try again.")

    # Input: Email Address
    while True:
        email = input("Enter your email address: ").strip()
        if is_valid_email(email):
            break
        else:
            print("Invalid email format. Please try again.")

    # Input: Phone Number
    while True:
        phone = input("Enter your phone number (10-15 digits): ").strip()
        if is_valid_phone(phone):
            break
        else:
            print("Invalid phone number. Please try again.")

    # Input: Password
    while True:
        password = input("Create a strong password: ").strip()
        if is_strong_password(password):
            break
        else:
            print("Password must be at least 8 characters long and include uppercase, lowercase, a number, and a special character.")

    # Account created
    print("\nAccount successfully created! Here are your details:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")

if __name__ == "__main__":
    create_customer_account()
