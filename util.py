def validate_email(email):
    import re
    p = re.compile(r"^[A-Za-z0-9]+([_\.][A-Za-z0-9]+)*@([A-Za-z0-9\-]+\.)+[A-Za-z]{2,6}$")
    return p.match(email)


def validate_phone(phone):
    import re
    p = re.compile(r"^1[3-9]\d{9}$")
    return p.match(phone)