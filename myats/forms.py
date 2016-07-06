from django import forms
from django.contrib.auth.models import User
class RegForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    check_pass = forms.CharField(label='Re-type Password', widget=forms.PasswordInput())
    user_email=forms.EmailField(label='Email')
    def clean(self):
        cleaned_data = super(RegForm, self).clean()
        password = cleaned_data.get('password')
        check_pass = cleaned_data.get('check_pass')
        if password != check_pass:
            raise forms.ValidationError('Passwords do not match.')
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError('This Username is taken.')
        if User.objects.filter(email=self.cleaned_data['user_email']).exists():
            raise forms.ValidationError('This email is already in use.')
        return cleaned_data
