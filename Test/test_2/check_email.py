def check_email(email: str) -> bool:
    if '@' in email and '.' in email and ' ' not in email:
        return True
    else:
        return False

if __name__ == "__main__":
    email = 'example@example.com'
    print(check_email(email))

    email = 'example @example .com'
    print(check_email(email))
