"""
User Stories
As a user, I want to create a password locker account with my details, a login username and password.
As a user, I want to store my already existing account credentials in the application. Assuming I already have a twitter account, I want to store my already existing twitter username and password in the application.
As a user, I want to create new account credentials in the application. For example, if I have not yet signed up for Instagram, I would want to create a credentials account for Instagram in the application and the application generates a password for me to use when I sign up for Instagram.
As a user, I want to have the option of putting in a password that I want to use for the new credential account. For example, when creating my Instagram credential account, I want to have an option of putting in the password I want to use instead of having the application generate a password for me.
As a user, I also want to view my various account credentials and their passwords in the application.
As a user, I want to delete a credentials account that I no longer need in the application.
Objectives
Your project should have two classes, a User class and Credentials class.
Your application should have an authentication system that enables a user to log into their account and view their credentials. A user should be able to login to their account using the password that they created and NOT any password.
Your project should make use of docstrings to document methods and functions.
Your project must have a test class that test each individual method in your classes.
"""

"""
Classes:

User class:
1. Initialise the user class with first name, last name, phone number, email address, Username and password  Once registered the user should be asked to log in again for activation.
After creation should not create another User again
2. The class can only be initialised once at joining. All other times the user has to be an existing user.
3. The class should have a method that creates the user and inserts their login credentials into the User credentials dictionary
4. The class should have a method to validate the user exists in the dictionary at log in
5. The class should have a class for the user to display their credentials using their username and password
6. The class should have a method for the user to change their username only and save and display the changes
7. The class should have a method for the user to change their password only and save and display the changes the changes
8. The class should have a method for the user to change their password and username.
"""


# def password_gen():
#     pass_word = []
#     password_characters = string.ascii_letters + string.digits + string.punctuation
#     password_length = random.randint(7, 17)
#     for p in range(password_length):
#         pass_word.append(random.choice(password_characters))
#         password = ''.join(pass_word)
#     # print(password)
#     return password


class User:
    user_list = list()
    """This dictionary contains a user's detailed information. It will be updated with the various class methods"""

    def __init__(self, first_name, last_name, phone_number, email, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.username = username
        self.password = password

    @classmethod
    def display_users(cls):
        """method that returns the user dictionary list"""
        return cls.user_list

    # def save_user(self):
    #     """ save user created on to the user dict in the dict class dict object"""
    #     User.UserDetails.update(
    #         {self.username: [self.first_name, self.last_name, self.phone_number, self.email, self.username,
    #                          self.password]})

    # This section will be activated later.
    # def delete_user(self):
    #     """delete_user method deletes saved user from the user dictionary"""
    #     User.UserDetails.pop(self.username)

    # @classmethod
    # def find_username_pw(cls, username):
    #     """method takes in username and password and returns the details that match it
    #     Args:
    #         username and password
    #     Returns:
    #         user details
    #         """
    #     for key, value in User.UserDetails.items():
    #         if key == username:
    #             return username
    #
    #     # for username in cls.UserDetails:
    #     #     if User.UserDetails['username'] == username:
    #     #         return username
    #     # [key for key, value in User.UserDetails.items() if key == username]
    #


"""

Credentials class

1. Class should have a dictionary
2. The class should be initialized by SocialMedia, username, Password (For accounts that are already existing)
3. New accounts should have the Socialmedia, username and a randomly generated password by the application or choose the password
4. Method for creating existing Accounts
5. Method for changing existing accounts username
6. Method for changing an existing Account password
7. Method for changing existing username and password
8. Method for displaying existing accounts
9. Method for deleting  existing accounts
"""
