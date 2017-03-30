from usersservices.models.user import find_user_by_email_and_password

def auth(email, password):
    user = find_user_by_email_and_password(email, password)
    return user

