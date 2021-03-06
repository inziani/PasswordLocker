#!/usr/bin/env python3.8
"""This the main program file that runs the password locker application"""
import sys
import time

from SocialMedia import SocialMedia
from User import User


def create_user(f_name, l_name, phone, email, user_name, pass_word):
    """Function to create a new User  in the application - User class"""
    new_user = User(f_name, l_name, phone, email, user_name, pass_word)
    User.user_list.append(new_user.first_name)
    User.user_list.append(new_user.last_name)
    User.user_list.append(new_user.phone_number)
    User.user_list.append(new_user.email)
    User.user_list.append(new_user.username)
    User.user_list.append(new_user.password)
    with open('users.txt', newline='', mode='a') as add_user:
        add_user.write('\n')
        add_user.write(str(User.user_list))
    return new_user


def social_media_acc(ss_platform, ss_username, ss_password):
    """Function to create a new social media account in the application - User class"""
    new_ss_account = SocialMedia(ss_platform, ss_username, ss_password)
    SocialMedia.social_media_accounts.append(new_ss_account.social_media_platform)
    SocialMedia.social_media_accounts.append(new_ss_account.username)
    SocialMedia.social_media_accounts.append(new_ss_account.password)
    with open('social_media.txt', newline='', mode='a') as add_account:
        add_account.write('\n')
        add_account.write(str(SocialMedia.social_media_accounts))
    return new_ss_account


def new_password():
    """This function calls the function generation method"""
    SocialMedia.pass_word()


def check_username(user_name):
    """This function checks if the new username  chosen by new user during
    account creation exists. Only non existence usernames are accepted. """
    old_user_name = list()
    with open('users.txt', 'r') as existing_username:
        for Line in existing_username:
            old_user_name = eval(Line)
            eva_user_name = list(','.join(old_user_name).split(','))
            if user_name == eva_user_name[4]:
                print('That user name is taken, pick another one and try again.')
                sys.exit()


def log_on(user_name, pass_word):
    """This is the log on function that checks if the user exists in the application."""
    user_log_on = list()
    with open('users.txt', 'r') as log_on_details:
        for Line in log_on_details:
            if user_name in Line:
                user_log_on = eval(Line)
                log_on_check = list(','.join(user_log_on).split(','))
                if str(user_name) != str(log_on_check[4]) or str(pass_word) != str(log_on_check[5]):
                    print('Invalid user name or password')
                    sys.exit()


def display_user_sm(plat_form):
    """This function is used to display the user details in the application. It needs to be modified
    to pick a specific person's information"""
    display_details = list()
    with open('social_media.txt', 'r') as display_username:
        for Line in display_username:
            if plat_form.lower() in Line:
                display_details = eval(Line)
                print(display_details)


def display_user(user_name):
    """This function is used to display the user details in the application. It needs to be modified
    to pick a specific person's information"""
    display_details = list()
    with open('users.txt', 'r') as display_username:
        for Line in display_username:
            if user_name in Line:
                display_details = eval(Line)
                print(display_details)


def modify_user_details(user_name):
    """This function is used to modify users in the User class"""
    changed_name = list()
    print('1 to modify your name \n'
          '2 to modify your phone number \n'
          '3 to modify your email \n'
          '4 to modify your username \n'
          '5 to modify your password  \n')

    modify_details = int(input())
    if modify_details == 1:
        change_details = list()
        new_first_name = input('Enter the new first name \n')
        new_last_name = input('Enter the new last name \n')
        with open('users.txt', 'r') as old_name:
            for Line in old_name:
                if user_name in Line:
                    change_details = eval(Line)
                    changed_list = list(','.join(change_details).split(','))
                    changed_list[0:2] = [new_first_name, new_last_name]
        with open('users.txt', 'w') as update_name:
            update_name.write(str(changed_list))
            print('Your new name is as follows')
            print(changed_list)

    elif modify_details == 2:
        new_phone_num = input('Enter the new phone number \n')
        with open('users.txt', 'r') as old_phone:
            for Line in old_phone:
                if user_name in Line:
                    change_details = eval(Line)
                    changed_list = list(','.join(change_details).split(','))
                    changed_list[2] = new_phone_num
        with open('users.txt', 'w') as update_phone:
            update_phone.write(str(changed_list))
            print('Your new phone number are as follows')
            print(changed_list)

    elif modify_details == 3:
        new_email = input('Enter the new email\n')
        with open('users.txt', 'r') as old_email:
            for Line in old_email:
                if user_name in Line:
                    change_details = eval(Line)
                    changed_list = list(','.join(change_details).split(','))
                    changed_list[3] = new_email
        with open('users.txt', 'w') as update_email:
            update_email.write(str(changed_list))
            print('Your new email are as follows')
            print(changed_list)

    elif modify_details == 4:
        new_username = input('Enter the new username \n')
        with open('users.txt', 'r') as old_username:
            for Line in old_username:
                if user_name in Line:
                    change_details = eval(Line)
                    changed_list = list(','.join(change_details).split(','))
                    changed_list[4] = new_username
        with open('users.txt', 'w') as update_username:
            update_username.write(str(changed_list))
            print('Your new username are as follows')
            print(changed_list)

    elif modify_details == 5:
        new_password = input('Enter the new password \n')
        with open('users.txt', 'r') as old_password:
            for Line in old_password:
                if user_name in Line:
                    change_details = eval(Line)
                    changed_list = list(','.join(change_details).split(','))
                    changed_list[5] = new_password
        with open('users.txt', 'w') as update_password:
            update_password.write(str(changed_list))
            print('Your new password is as follows')
            print(changed_list)
    else:
        print('invalid code')


def delete_user(user):
    """This function is used to  to delete a user in the user class"""
    user.delete_user()


def main():
    """This is the main function that is used to run the whole application"""
    print('Hello, welcome to our social media accounts app. What is your name?')
    print('\n')
    user_name = input()

    print(f'Hi, {user_name} \n'
          f' nu - Visitor - Create an account with us \n'
          f' eu - Maintain your account with us \n'
          f' ss - Manage your social media accounts')
    print('\n')

    user_status = input().lower()

    if user_status == 'nu':
        print('fill in the details below to create a new account')

        print('First name..')
        f_name = input().title()

        print('Last name..')
        l_name = input().title()

        print('Phone number...')
        phone = input()

        print('Your email..')
        email = input()

        print('Preferred username..')
        user_name = input()
        check_username(user_name)

        print('Password..')
        pass_word = input()

        create_user(f_name, l_name, phone, email, user_name, pass_word)
        print(
            ' Your account + ' '{} {}'.format(f_name,
                                              l_name) + ' ' + 'has been created, log in with your username '
                                                              'and password to activate it.')
        time.sleep(int(3))

    elif user_status == 'eu' or user_status == 'ss':
        print('Please log in with your username and password \n'
              'User name')
        user_name = input()

        print('Password')
        pass_word = input()
        log_on(user_name, pass_word)

        # Log on function
        print('Use these short codes to select the service you want:\n'
              'dd : Display your details \n'
              'cg : Edit your details \n'
              's1 : create a social media account \n'
              's2 : display your social media accounts \n'
              's3 : delete a social medial account \n'
              'ex : exit')
        short_code = input().lower()

        if short_code == 'dd':
            print('Key in your username')
            user_name = input()
            print('Your details on file..')
            display_user(user_name)

        elif short_code == 'cg':
            print('Enter your username')
            user_name = input()
            modify_user_details(user_name)

        elif short_code == 's1':
            print('create new social media account')

            print('Social media platform..')
            ss_platform = input().title()

            print('Username..')
            ss_username = input().title()

            print('Password...\n')
            ss_password = input()

            social_media_acc(ss_platform, ss_username, ss_password)
            print(
                ' Your account + ' '{} {} {}'.format(ss_platform,
                                                     ss_username, ss_password) + ' ' + 'has been created.')
            time.sleep(int(3))

        if short_code == 's2':
            print('Key in the social media plat form')
            plat_form = input()
            print('Your details on file..')
            display_user_sm(plat_form)

        elif short_code == 'ex':
            print('Goodbye')

        else:
            print('Please enter a valid short code')

    else:
        print('Type yes or no, goodbye')


if __name__ == '__main__':
    main()
