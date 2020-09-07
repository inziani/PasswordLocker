
class User:
    user_list = list()
    """This list contains a user's detailed information. It will be updated with the various class methods
    and functions"""

    def __init__(self, first_name, last_name, phone_number, email, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.username = username
        self.password = password

