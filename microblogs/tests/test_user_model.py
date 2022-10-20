from symbol import factor
from django.core.exceptions import ValidationError
from django.test import TestCase
from microblogs.models import User

class UserModelTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            '@johndoe',
            first_name ='John',
            last_name='Doe',
            email = 'johndoe@example.org',
            password = 'password123',
            bio = 'the quick brown fox'
        )

    def test_valid_user(self):
        self.__assert_user_is_valid()
        

    def test_username_cannot_be_blank(self):
        self.user.username=''
        self.__assert_user_is_invalid()

    def test_username_can_be_30_characters_long(self):
        self.user.username = '@' + 'x' * 29
        self.__assert_user_is_valid()

    def test_username_cannot_be_30_characters_long(self):
        self.user.username = '@' + 'x' * 30
        self.__assert_user_is_invalid()
    
    def test_username_must_be_unique(self):
        user2 = self.__create_second_user()
        self.user.username = '@janedoe'
        self.__assert_user_is_invalid()
    
    def test_username_must_start_with_at_symbol(self):
        self.user.username='johndoe'
        self.__assert_user_is_invalid()

    def test_username_must_contain_only_alphanumericals_after_at(self):
        self.user.username='@john@doe'
        self.__assert_user_is_invalid()
    
    def test_username_must_have_minimum_three_alphanumericals_after_at(self):
        self.user.username='@jo'
        self.__assert_user_is_invalid()
    
    def test_username_may_contain_numbers(self):
        self.user.username='@j0hndoe2'
        self.__assert_user_is_valid()
    
    def test_username_must_contain_only_1_at(self):
        self.user.username='@johndoe@'
        self.__assert_user_is_invalid()

###### Create tests 

    def test_first_name_is_not_blank(self):
        self.user.first_name = ''
        self.__assert_user_is_invalid()

    def test_first_name_is_not_unique(self):
        user2 = self.__create_second_user()
        user2.first_name = self.user.first_name
        self.__assert_user_is_valid()
   
    def test_first_name_is_not_over_50(self):
        self.user.first_name = 'x' * 51
        self.__assert_user_is_invalid()

    def test_last_name_is_not_blank(self):
        self.user.last_name = ''
        self.__assert_user_is_invalid()

    def test_last_name_is_not_unique(self):
        user2 = self.__create_second_user()
        user2.last_name = self.user.last_name
        self.__assert_user_is_valid()
   
    def test_last_name_is_not_over_50(self):
        self.user.last_name = 'x' * 51
        self.__assert_user_is_invalid()

    
    def test_email_is_unique(self):
        user2 = self.__create_second_user()
        self.user.email = user2.email
        self.__assert_user_is_invalid()

    def test_email_starts_has_at(self):
        self.user.email = "johndoe.example.org"
        self.__assert_user_is_invalid()
       
    


    def __assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except (ValidationError):
            self.fail('test user should be valid')

    def __assert_user_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.user.full_clean()

    def __create_second_user(self):
        user = User.objects.create_user(
            '@janedoe',
            first_name ='jane',
            last_name='Doe',
            email = 'janedoe@example.org',
            password = 'password123',
            bio = 'This is my bio'
        )
        return user


  


    