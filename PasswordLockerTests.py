import unittest

from User import User


class MyTestCase(unittest.TestCase):
    """ Test class that defines test cases for the User and Credentials  class behaviours
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases"""

    def setUp(self):
        """set up method to run before each test cases"""
        self.new_user = User('Valentine', 'Robai', '0712345678', 'ValentineRobai.Inziani@gmail.com', 'vrobai',
                             'password')

    def test_init(self):
        self.assertEqual(self.new_user.first_name, 'Valentine')
        self.assertEqual(self.new_user.last_name, 'Robai')
        self.assertEqual(self.new_user.phone_number, '0712345678')
        self.assertEqual(self.new_user.email, 'ValentineRobai.Inziani@gmail.com')
        self.assertEqual(self.new_user.username, 'vrobai')
        self.assertEqual(self.new_user.password, 'password')

    def test_save_user(self):
        """test_save_user test case to test if the user object is saved into the user list"""
        self.new_user.save_user()
        self.assertEqual(len(User.UserDetails), 1)

    def tearDown(self):
        """tear down method does clean up after each test case has run"""
        User.UserDetails = dict()

    def test_save_multiple_users(self):
        """test_save_multiple_users to check if we can save multiple users with different usernames """
        self.new_user.save_user()
        test_user = User('Sophia', 'Robai', '0722857832', 'ValentineRobai.@gmail.com', 'val',
                         'password')
        test_user.save_user()
        self.assertEqual(len(User.UserDetails), 2)

    def test_delete_user(self):
        """test_delete_user to test if we can delete their account """

        self.new_user.save_user()
        test_user = User('Sophia', 'Robai', '0722857832', 'ValentineRobai.@gmail.com', 'val',
                         'password')
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.UserDetails), 1)

    # def test_find_userdetails(self):
    #     """test to check if we can find a contact by username and password then display their information"""
    #     self.new_user.save_user()
    #     test_user = User('Sophia', 'Robai', '0722857832', 'ValentineRobai.@gmail.com', 'val',
    #                      'password')
    #     test_user.save_user()
    #     found_user = User.find_username_pw('val')
    #     self.assertEqual(found_user.first_name, test_user.first_name)
    #     # self.assertEqual(User.found_user)

    def test_display_all_users(self):
        """method that returns a list of all contacts saved"""
        self.assertEqual(User.display_users(), User.UserDetails)


if __name__ == '__main__':
    unittest.main()
