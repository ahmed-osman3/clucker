import imp
from django import forms
from django import forms
from .models import User
from django.core.validators import RegexValidator

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','bio']
        widgets = {'bio' : forms.Textarea()}

    password = forms.CharField(
        label = "Password", 
        widget=forms.PasswordInput(),
        validators=[
            RegexValidator(
            regex = r'[A-Z]', # ^ = circumflex symbol. corresponds to beginning of string. $ = ending of string. 
            message = 'Password must have an uppercase symbol'
            ),
            RegexValidator(
             regex=r'[a-z]',
            message='Password must contain an uppercase character'
            ),
            RegexValidator(
             regex=r'[0-9]',
            message='Password must contain a number'
            ),
         ]
        )


    password_confirmation = forms.CharField(
        label = "Password Confirmation",
         widget=forms.PasswordInput()
         )
    
    def clean(self):
        super().clean()
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if password != password_confirmation:
            self.add_error('password_confirmation','Conirmation does not match password')
         