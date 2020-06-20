from django import forms
from django.db import transaction
from django.contrib.auth.forms import ReadOnlyPasswordHashField
# from .models import Individual, Doctor, Recruiter, User
from allauth.account.forms import SignupForm, LoginForm
from .models import User
from django.forms import ModelForm
from django.conf import settings
from django.utils.translation import gettext, gettext_lazy as _, pgettext

class UserLoginForm(LoginForm):
    '''
    user login form
    '''
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }), label='')


    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(LoginForm, self).__init__(*args, **kwargs)
        login_widget = forms.TextInput(attrs={'placeholder':
                                                  ('Username or e-mail'),
                                                  'class':'form-control',
                                                  'autofocus': 'autofocus'})
        login_field = forms.CharField(label=pgettext("field label",
                                                         "Login"),
                                          widget=login_widget)


        self.fields["login"] = login_field



class PasswordField(forms.CharField):

    def __init__(self, *args, **kwargs):
        kwargs['widget'] = forms.PasswordInput(attrs={'placeholder': kwargs.get("label"),
                                                      'class': 'form-control',
                                                      })
        super(PasswordField, self).__init__(*args, **kwargs)


class UserSignUpForm(SignupForm):
        '''
        user signup form
        '''


        username = forms.CharField(widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder': 'Username'
        }), label='')
        email = forms.EmailField(widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        }), label='')
        password1 = forms.CharField(widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        }), label='')

        password2 = forms.CharField(widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password Confirmation'
        }), label='')

        field_order = ['username','email','password1', 'password2']


        def __init__(self, *args, **kwargs):
            super(SignupForm, self).__init__(*args, **kwargs)
            self.fields['password1'] = forms.CharField(widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }), label='')
            # if app_settings.SIGNUP_PASSWORD_ENTER_TWICE:
            self.fields['password2'] = forms.CharField(widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Password'
            }), label='')

            self.fields['email'].label=""
