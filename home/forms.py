from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SearchForm(forms.Form):
    query = forms.CharField(label='Search',max_length=100)
    catid = forms.IntegerField()

class SignUpForm(UserCreationForm):

    username = forms.CharField(max_length=30, label='User Name')
    email = forms.EmailField(max_length=30, label='Email', help_text='Required. Inform a valid email address.')
    first_name = forms.CharField(max_length=30, help_text='First Name', label='First Name :')
    last_name = forms.CharField(max_length=30, help_text='First Name',  label='Last Name : ')


    class Meta:
        model = User
        fields = ('username',  'email','first_name','last_name', 'password1', 'password2',)