import re

def is_valid_email(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email) is not None

# ইউজারের ইনপুট নেওয়া
email = input("Enter your email ID: ").strip()

# ইমেইল ভ্যালিড চেক
if is_valid_email(email):
    print(f"'{email}' is a valid email ID.")
else:
    print(f"'{email}' is NOT a valid email ID.")

