import re

def is_valid_email(email):
    """Check if the email format is valid."""
    pattern = r'^[\w.-]+@[\w.-]+\.\w{2,}$'
    return re.match(pattern, email) is not None

def is_valid_phone(phone):
    """Check if the phone number is valid (10-15 digits)."""
    return phone.isdigit() and 10 <= len(phone) <= 15

def is_strong_password(password):
    """Check if the password is strong (minimum 8 characters, maximum 30 characters, includes uppercase, lowercase, number, and special character)."""
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,30}$'
    return re.match(pattern, password) is not None

def explain_password_issues(password):
    """Explain why a password is invalid."""
    issues = []
    if len(password) < 8 or len(password) > 30:
        issues.append("Password must be between 8 and 30 characters.")
    if not any(char.islower() for char in password):
        issues.append("Password must include at least one lowercase letter.")
    if not any(char.isupper() for char in password):
        issues.append("Password must include at least one uppercase letter.")
    if not any(char.isdigit() for char in password):
        issues.append("Password must include at least one number.")
    if not any(char in '@$!%*?&' for char in password):
        issues.append("Password must include at least one special character (@$!%*?&).")
    return issues

def get_retype_password():
    """Ensure the password is retyped correctly."""
    while True:
        password = input("Create a strong password (8-30 characters): ").strip()
        issues = explain_password_issues(password)
        if issues:
            print("Invalid password:")
            for issue in issues:
                print(f"- {issue}")
            continue
        retype_password = input("Retype your password: ").strip()
        if password == retype_password:
            return password
        else:
            print("Passwords do not match. Please try again.")

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
    password = get_retype_password()

    # Account created
    print("\nAccount successfully created! Here are your details:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")

def password_input_and_output():
    """Handles password creation, validation, and retype confirmation."""
    while True:
        password = input("Create a strong password (8-30 characters): ").strip()
        issues = explain_password_issues(password)
        if issues:
            print("Invalid password:")
            for issue in issues:
                print(f"- {issue}")
            continue
        retype_password = input("Retype your password: ").strip()
        if password == retype_password:
            print("Password successfully set!")
            return password
        else:
            print("Passwords do not match. Please try again.")

# Example usage:
if __name__ == "__main__":
    password = password_input_and_output()
