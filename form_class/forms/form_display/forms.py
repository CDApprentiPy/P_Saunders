from django import forms


class UserForm(forms.Form):

    name = forms.CharField(label='Name', max_length=100)
    birthday = forms.DateTimeField(label='Birthday')
    email = forms.EmailField(label='email')
    password = forms.CharField(label='password', widget=forms.PasswordInput())