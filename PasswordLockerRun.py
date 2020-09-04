import time

from User import User


def create_user(f_name, l_name, phone, email, user_name, pass_word):
    """Function to create a new User """
    new_user = User(f_name, l_name, phone, email, user_name, pass_word)
    return new_user


def save_user(user):
    """ method to save new users"""
    user.save_user()


def delete_user(user):
    """method to delete a user"""
    user.delete_user()


def find_username(username):
    """Find user by password and username"""
    return User.find_username_pw(username)


def display_users():
    return User.display_users()


def main():
    print('Hello, welcome to our social media accounts app. What is your name?')
    print('\n')
    user_name = input()

    print(f'{user_name}, Type yes for a  returning existing user \n'
          f'No if you want to register')
    print('\n')

    user_status = input().lower()
    if user_status == 'yes':
        while True:
            print('Use these short codes to select the service you want:\n'
                  'cc : Create a new account \n'
                  'da : Manage your account \n'
                  'ds : Manage your social media accounts\n'
                  'ex : exit')

            short_code = input().lower()

            if short_code == 'cc':
                print('Welcome to social media manager.')

                print('First name..')
                f_name = input()

                print('Last name..')
                l_name = input()

                print('Phone number...')
                phone = input()

                print('Your email..')
                email = input()

                print('Preferred username..')
                user_name = input()
                if user_name in User.UserDetails:
                    print('That user name has been taken, please choose another one.')
                else:
                    pass

                print('Password..')
                pass_word = input()

                save_user((create_user(f_name, l_name, phone, email, user_name, pass_word)))
                print(
                    ' Your account + ' '{} {}'.format(f_name,
                                                      l_name) + ' ' + 'has been created, log in with your username '
                                                                      'and password to activate it.')
                time.sleep(int(3))
            elif short_code == 'da':
                print('Manage my account')

            else:
                print('Please enter a valid short code')
            break

    elif user_status == 'no':
        print('Use these short codes to select the service you want:\n'
              'cc : Create a new account \n'
              'ex : exit')

        short_code = input().lower()

        if short_code == 'cc':
            print('Welcome to social media manager.')

            print('First name..')
            f_name = input()

            print('Last name..')
            l_name = input()

            print('Phone number...')
            phone = input()

            print('Your email..')
            email = input()

            print('Preferred username..')
            user_name = input()
            if user_name in User.UserDetails:
                print('That user name has been taken, please choose another one.')
            else:
                pass

            print('Password..')
            pass_word = input()

            save_user((create_user(f_name, l_name, phone, email, user_name, pass_word)))
            print(
                ' Your account + ' '{} {}'.format(f_name,
                                                  l_name) + ' ' + 'has been created, log in with your username '
                                                                  'and password to activate it.')
            time.sleep(int(3))
        elif short_code == 'ex':
            print('Goodbye')

        else:
            print('Please enter a valid short code')

    else:
        print('Type yes or no, goodbye')


if __name__ == '__main__':
    main()
