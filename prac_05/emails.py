def main():
    """Creating dictionary"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        confirm = input(f"Is your name {name}? (Y/n) ")
        if confirm.upper() != "Y" and confirm != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def get_name(email):
    """Obtaining name from email"""
    username = email.split('@')[0]
    name_parts = username.split('.')
    name = " ".join(name_parts).title()
    return name
main()