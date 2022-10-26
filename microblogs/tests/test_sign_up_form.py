from django import forms
from django.test import TestCase
from microblogs.forms import SignUpForm
from microblogs.models import User
from django.contrib.auth.hashers import check_password


class SignUpFormTestCase(TestCase):
    
    def setUp(self):
        self.form_input = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'username': '@janedoe',
            'email':'janedoe@example.org',
            'bio': 'My bio',
            'password': 'Password123',
            'password_confirmation': 'Password123',
        }

#form accepts valid input data
    def test_valid_sign_up_form(self):
        form = SignUpForm(data = self.form_input)
        self.assertTrue(form.is_valid())

#form has necessary fields
    def test_form_has_necessary_fields(self):
        form = SignUpForm()
        self.assertIn('first_name', form.fields)
        self.assertIn('last_name', form.fields)
        self.assertIn('username', form.fields)
        self.assertIn('email', form.fields)
        email_field = form.fields['email']
        self.assertTrue(isinstance(email_field, forms.EmailField))
        self.assertIn('bio', form.fields)
        self.assertIn('password', form.fields)
        passwordWidget = form.fields['password'].widget
        self.assertTrue(isinstance(passwordWidget,forms.PasswordInput))
        self.assertIn('password_confirmation', form.fields)
        passwordConfirmWidget = form.fields['password_confirmation'].widget
        self.assertTrue(isinstance(passwordConfirmWidget,forms.PasswordInput))


#form users model validation
    def test_form_uses_model_validation(self):
        self.form_input['username'] = 'badusername'
        form = SignUpForm(data = self.form_input)
        self.assertFalse(form.is_valid())

#New password has correct format
    def test_password_must_contain_uppercase_character(self):
        self.form_input['password'] = 'password123'
        self.form_input['password_confirmation'] = 'password123'
        form = SignUpForm(data = self.form_input)
        self.assertFalse(form.is_valid())

    def test_password_must_contain_lowercase_character(self):
        self.form_input['password'] = 'PASSWORD123'
        self.form_input['password_confirmation'] = 'PASSWORD123'
        form = SignUpForm(data = self.form_input)
        self.assertFalse(form.is_valid())

    def test_password_must_contain_number(self):
        self.form_input['password'] = 'Password'
        self.form_input['password_confirmation'] = 'Password'
        form = SignUpForm(data = self.form_input)
        self.assertFalse(form.is_valid())
    
    def test_password_and_password_confirmation_are_identical(self):
        self.form_input['password'] = 'Password123'
        self.form_input['password_confirmation'] = 'Password'
        form = SignUpForm(data = self.form_input)
        self.assertFalse(form.is_valid())

    def test_form_must_save_correctly(self):
        form = SignUpForm(data = self.form_input)
        before_count = User.objects.count()
        form.save()
        user = User.objects.get(username = '@janedoe')
        self.assertEqual(user.first_name,'Jane')
        self.assertEqual(user.last_name,'Doe')
        self.assertEqual(user.email,'janedoe@example.org')
        self.assertEqual(user.bio,'My bio')
        is_password_correct = check_password('Password123',user.password)
        self.assertTrue(is_password_correct)


#New password and password confirmation must be identical.
