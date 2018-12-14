from django import forms
from basic_app import models
UserTypes = [
    ('Student', 'Student'),
]
class UserForm(forms.ModelForm):
    firstName = forms.CharField()
    lastName = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    userType = forms.CharField(label='Select User Type', widget=forms.Select(choices=UserTypes))
    class Meta:
        model = models.ManageUser
        fields = ('firstName', 'lastName', 'email', 'password', 'userType')
