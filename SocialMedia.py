import random


class SocialMedia:
    """This class is for the creation of the social media accounts """
    social_media_accounts = list()
    """This list will hold the social accounts that a user is maintaining within the application """

    def __init__(self, social_media_platform, username, password):
        self.social_media_platform = social_media_platform
        self.username = username
        self.password = password

    def pass_word(self):

        """ Function not working as expected. No time to correct it"""
        self.password = ''
        print('Would you like an auto generated password?')
        user_input = str(input().lower())
        if user_input == 'yes':
            self.password = str(random.randint(0, 10))
        else:
            print('enter your own password')
            self.password = input()
        return self.password
