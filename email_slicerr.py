def email_slicer():
    while True:
        email = input("Enter Your Email: ").strip()

        # Input validation
        if "@" not in email or "." not in email[email.index("@"):]:
            print("Invalid email. Please enter a valid email address with '@' and a domain.")
            continue

        # Extract username and domain
        try:
            username = email[:email.index("@")]
            domain_name = email[email.index("@") + 1:]

            # Format the output
            format_ = (f"Your username is '{username}' and your domain is '{domain_name}'")
            print(format_)

            # Save to file
            with open("email_details.txt", "a") as file:
                file.write(f"Email: {email}, Username: {username}, Domain: {domain_name}\n")

            print(f"Details saved to 'email_details.txt'.")
            break

        except Exception as e:
            print(f"An error occurred: {e}")
            continue


if __name__ == "__main__":
    email_slicer()
