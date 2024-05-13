from check_email import check_email

def test_check_email_valid():
    assert check_email('example@example.com') == True

def test_check_email_invalid():
    assert check_email('example @example .com') == False
